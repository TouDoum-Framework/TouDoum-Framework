from glob import glob
from importlib import import_module
import re


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
    modules = []
    for module_dir in glob("server/modules/*/urls.py"):
        modules.append(re.sub("server/modules/src/|/urls\.py", "", module_dir))
    return modules
