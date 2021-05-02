from glob import glob
from importlib import import_module
import re


def loadModules() -> list:
    return [module.replace("/", ".") for module in glob("server/modules/*")]


def getUrls(t: str) -> list:
    urls = []
    for module_dir in glob("server/modules/*/urls.py"):
        module_name = re.sub("server/modules/|/urls\.py", "", module_dir)
        module = import_module("server.modules." + module_name + ".urls", ".")
        if t == "api":
            urls = urls + module.url_api
        elif t == "panel":
            urls = urls + module.url_panel
    return urls
