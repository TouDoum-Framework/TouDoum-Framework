class Plugin:

    name = ""         # give a name to plugin
    description = ""  # describe what do this plugin
    version = ""      # version of plugin
    protocol = ""     # "TCP" "UDP" or "TCP|UDP"
    author = ""       # your name here

    def scan(self):
        pass

    def attack(self):
        pass
