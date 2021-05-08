import importlib
import re
from glob import glob


class PluginManager:
    plugins: list
    download: list

    def __init__(self, plugins: list):
        self.plugins = []
        self.download = []
        self.load(plugins)

    def load(self, plugins: list):
        for plugin_file in glob("./client/plugins/*.py"):
            plugin_name = re.sub("\./client/plugins/|\.py", "", plugin_file)
            module = importlib.import_module("client.plugins." + plugin_name, ".")

            obj = module.Plugin()
            obj.file = plugin_name
            obj.file = plugin_name
            if obj.name in plugins:
                plugins.remove(obj.name)
                print("Loaded plugin " + obj.name)
                self.plugins.append(obj)

        self.download = plugins

    def reload(self, plugins: list):
        self.plugins = []
        self.download = []
        self.load(plugins)