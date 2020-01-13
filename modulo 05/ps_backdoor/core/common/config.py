from configobj import ConfigObj


class Settings(object):
    def __init__(self):
        self.conf = ConfigObj('core/config/app.ini')


    def getValue(self, key):
        try:
            return self.conf[key]
        except KeyError:
            return None

    def setValue(self, key, value):
        self.conf[key] = value
        self.conf.write()

    def getPayloadStatus(self, plugin_name):
        try:
            return self.conf["plugin"].as_bool(plugin_name)
        except KeyError:
            return None

    def setPayloadStatus(self, plguin_name,  status):
        self.conf['plugin'][plguin_name] = status
        self.conf.write()