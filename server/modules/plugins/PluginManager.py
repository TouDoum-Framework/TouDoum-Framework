import importlib
import re
from glob import glob

function_require_plugin = [
    "scan",
    "attack"
]
var_require_plugin = [
    "name",
    "description",
    "version",
    "protocol",
    "author"
]


class PluginManager:
    plugins: list = []
    error: list = []

    # @arg plugin_list : list of plugin to load
    def __init__(self):
        self.load()

    # Load and initialise all plugin in plugins directory
    def load(self):
        for plugin_file in glob("server/modules/plugins/*.py"):

            plugin_name = re.sub("server/modules/plugins/|\.py", "", plugin_file)
            module = importlib.import_module("plugins." + plugin_name, ".")

            obj = module.Plugin()
            obj.file = plugin_name
            obj_content = dir(obj)

            # check if plugin contain all default function for run
            if len(set(obj_content) & set(function_require_plugin)) == len(function_require_plugin):
                # check if plugin information is set
                if len(set(obj_content) & set(var_require_plugin)) == len(var_require_plugin):
                    self.plugins.append(obj)
                else:
                    self.error.append("Error the '" + plugin_name +
                                      "' plugin does not contain the required information to be correctly loaded")
            else:
                self.error.append("Error the '" + plugin_name +
                                  "' plugin does not contain the required functions to be correctly loaded")

    def reload(self, plugin_list: str = None):
        self.plugins.clear()
        self.error.clear()
        self.load()
