import importlib
import os

from utils.celery import reject_task


class ModulesLoader:

    def __init__(self):
        self.loaded_modules = []  # list of tuples (module_name, module_object)

    def get_module_object(self, module_name: str):
        for module in self.loaded_modules:
            if module[0] == module_name:
                return module[1]

    def is_module_loaded(self, module_name: str) -> bool:
        for module in self.loaded_modules:
            if module[0] == module_name:
                return True
        return False

    def load_module(self, module_name: str):
        path_main_file = f"modules/{module_name}/main.py"
        # check if file exists
        if not os.path.isfile(path_main_file):
            reject_task(f"Entry point file (main.py) for module {module_name} not found")

        # check if module is already loaded
        if self.is_module_loaded(module_name):
            print("Module " + module_name + " already loaded")
        else:
            # load module
            module = importlib.import_module(f"client.modules.{module_name}.main")
            self.loaded_modules.append((module_name, module,))
            print("Module " + module_name + " loaded")
