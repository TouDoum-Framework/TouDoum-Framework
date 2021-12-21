from django.apps import AppConfig
from glob import glob
from django.urls import path, include
from json import load as json_load
import re


class ModulesConfig(AppConfig):
    name = 'server.modules'


def load_modules() -> list:
    return [module.replace("\\", ".").replace("/", ".") for module in glob("server/modules/src/*")]


def sort_by_key_asc(data: list, key: str) -> len:
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


def sync_db() -> None:
    from server.modules.models import Module

    module_list = []
    # temp purge all module on db for proper register
    Module.objects.all().delete()

    for module_config_file in glob("server/modules/src/*/config.json"):
        with open(module_config_file) as content:
            module_list.append(json_load(content))

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


def get_urls(file: str) -> list:
    print("Loading module for " + file)

    urls = []
    for module_dir in glob("server/modules/src/*/urls/" + file + ".py"):
        module_name = re.sub("server/modules/src/|/urls/[a-z]+.py", "", module_dir.replace("\\", "/"))
        python_path = "server.modules.src." + module_name + ".urls." + file
        if file == "panel":
            urls.append(path('panel/module/' + module_name + '/', include(python_path)))
        elif file == "api":
            urls.append(path(r"api/ext/" + module_name + "/", include(python_path)))
    return urls


def get_client_file(module: str) -> list:
    return [re.sub("server/modules/src/" + module + "/client/", "", cf) for cf in
            glob("server/modules/src/" + module + "/client/**/*.py", recursive=True)]
