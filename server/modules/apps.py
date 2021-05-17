from django.apps import AppConfig
from glob import glob
from django.urls import path
from importlib import import_module
import re

from django.http import FileResponse


class ModulesConfig(AppConfig):
    name = 'modules'


def load_modules() -> list:
    return [module.replace("/", ".") for module in glob("server/modules/src/*")]


def get_modules_name() -> list:
    return [re.sub("server/modules/src/|/urls\.py", "", module_dir) for module_dir in glob("server/modules/*/urls.py")]


def syncDB() -> None:
    from server.modules.models import Module
    from server.cluster.urls import registerMaster
    master = registerMaster()
    for module_dir in glob("server/modules/src/*/apps.py"):
        module_name = re.sub("server/modules/src/|/apps\.py", "", module_dir)
        module = import_module("server.modules.src." + module_name + ".apps", ".")
        mod = Module.objects.filter(name=module.name).first()
        if mod is None:
            mod = Module()
            mod.name = module.name
            mod.version = module.version
            mod.save()
        mod.availableAt.add(master.pk)


def get_urls(t: str) -> list:
    urls = []
    for module_dir in glob("server/modules/src/*/urls.py"):
        module_name = re.sub("server/modules/src/|/urls\.py", "", module_dir)
        python_path = "server.modules.src." + module_name + ".urls"
        urls += path(module_name, python_path)
    return urls


def get_client_file(module: str) -> list:
    return [re.sub("server/modules/src/" + module + "/client/", "", cf) for cf in
            glob("server/modules/src/" + module + "/client/**/*.py", recursive=True)]


def download_client_file(module: str, file: str) -> FileResponse:
    file = open("server/modules/src/" + module + "/client/" + file, 'rb')
    print(file)
    return FileResponse(file)
