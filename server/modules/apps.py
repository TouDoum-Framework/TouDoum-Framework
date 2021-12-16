from django.apps import AppConfig
from glob import glob
from django.urls import path, include
from importlib import import_module
from json import loads as json_loads
import re


class ModulesConfig(AppConfig):
    name = 'server.modules'


def load_modules() -> list:
    return [module.replace("\\", ".").replace("/", ".") for module in glob("server/modules/src/*")]


def get_modules_name() -> list:
    return [re.sub("server/modules/src/|/apps.py", "", module_dir.replace("\\", "/"))
            for module_dir in glob("server/modules/*/apps.py")]


def sync_db() -> None:
    from server.modules.models import Module
    for module_dir in glob("server/modules/src/*/apps.py"):
        module_name = re.sub("server/modules/src/|/apps.py", "", module_dir.replace("\\", "/"))
        module = import_module("server.modules.src." + module_name + ".apps", ".")
        mod = Module.objects.filter(name=module.name).first()
        if mod is None:
            mod = Module()
            mod.name = module.name
            mod.version = module.version
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
