from re import sub
from shutil import rmtree
from glob import glob
from client.Api import Api


class ModulesLoader:
    modules: list

    def __init__(self, modules_required: list):
        self.modules = []
        self.load(modules_required)

    def load(self, modules_required: list = None):
        for modules_dir in glob("client/modules/*/main.py"):
            modules_dir = modules_dir.replace("\\", "/")
            modules_name = sub("client/modules/|/main.py", "", modules_dir)

            if modules_name in modules_required:
                print("[OK] Modules " + modules_name)
                modules_required.remove(modules_name)
                continue
            else:
                print("[RM] Module " + modules_name + " not required removing from modules folder")
                rmtree("client/modules/" + modules_name)
                continue

        if len(modules_required) > 0:
            api: Api = Api()
            api.get_modules_from_list(modules_required)
            self.load(modules_required)
