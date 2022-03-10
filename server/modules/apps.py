from re import sub, match
from os import walk
from utils.files import md5sum
from glob import glob
from json import load as json_load

from django.apps import AppConfig
from django.urls import path, include


class ModulesConfig(AppConfig):
    name = 'server.modules'


def load_modules() -> list:
    return [module.replace("\\", ".").replace("/", ".") for module in glob("modules/*")]


def sort_by_key_asc(data: list, key: str) -> list:
    new_data = []
    max_len = 0
    index_len = 0

    for item in data:
        item_len = len(item[key])
        if item_len > max_len:
            max_len = item_len

    while index_len <= max_len:
        for item in data:
            item_len = len(item[key])
            if item_len == index_len:
                new_data.append(item)
        index_len += 1

    return new_data


def sync_modules_db() -> None:
    from server.modules.models import Module, ModuleFile

    module_list = []
    # temp purge all module on db for proper register
    ModuleFile.objects.all().delete()
    Module.objects.all().delete()

    for module_config_file in glob("modules/*/config.json"):
        if match(r"modules/[\w\d]*/config\.json", module_config_file.replace("\\", "/")):
            with open(module_config_file) as content:
                module_list.append(json_load(content))
        else:
            print("Error for name of module " +
                  sub("modules/|/urls/[a-z]+.py", "", module_config_file.replace("\\", "/")))

    # register module on db with information given by config.json
    for item in sort_by_key_asc(module_list, "depend_on"):
        mod = Module()
        mod.name = item["name"]
        mod.display_name = item["display_name"]
        mod.description = item["description"]
        mod.version = item["version"]
        mod.author = item["author"]
        mod.repo = item["repo"]

        if len(item["depend_on"]) > 0:
            for mod_name in item["depend_on"]:
                mod.depend_on.add(Module.objects.filter(name=mod_name).first())

        mod.save()

        # register all file of current modules
        for root, dirs, files in walk('modules/'):
            for file in files:
                if "__pycache__" not in root:
                    mod_file = ModuleFile()
                    mod_file.module = mod
                    mod_file.name = file
                    mod_file.path = root
                    mod_file.checksum = md5sum(root + "/" + file)
                    mod_file.is_client = bool(match(r"modules/[\w\d]*/client", root))
                    mod_file.save()


def get_urls(file: str) -> list:
    print("Loading module for " + file)

    urls = []
    for module_dir in glob("modules/*/urls/" + file + ".py"):
        module_name = sub("modules/|/urls/[a-z]+.py", "", module_dir.replace("\\", "/"))
        python_path = "modules." + module_name + ".urls." + file
        if file == "panel":
            urls.append(path('panel/module/' + module_name + '/', include(python_path)))
        elif file == "api":
            urls.append(path(r"api/ext/" + module_name + "/", include(python_path)))
    return urls


def get_client_file(module: str) -> list:
    return [sub("modules/" + module + "/client/", "", cf) for cf in
            glob("modules/" + module + "/client/**/*.py", recursive=True)]
