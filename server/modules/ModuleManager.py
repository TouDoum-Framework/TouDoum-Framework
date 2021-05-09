from glob import glob
from importlib import import_module
import re


def syncDB():
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


def load_modules() -> list:
    return [module.replace("/", ".") for module in glob("server/modules/src/*")]


def get_urls(t: str) -> list:
    urls = []
    for module_dir in glob("server/modules/src/*/urls.py"):
        module_name = re.sub("server/modules/src/|/urls\.py", "", module_dir)

        module = import_module("server.modules.src." + module_name + ".urls", ".")
        if t == "api":
            urls = urls + module.url_api
        elif t == "panel":
            urls = urls + module.url_panel
    return urls


def get_modules_name():
    return [re.sub("server/modules/src/|/urls\.py", "", module_dir) for module_dir in glob("server/modules/*/urls.py")]
