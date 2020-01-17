


class BasePayload(object):
    _name = "Default"
    _code = None
    _activated = False
    _conf = None 
    _stager_path = ""

    def setHandler(self, IP, PORT):
        d = dict()
        d['SERVER'] = IP
        d['PORT'] = PORT
        self.setCode(d)

    def setActivated(self, status):
        self._activated = status

    def getActivated(self):
        return self._activated

    def readStager(self):
        with open(self._stager_path, 'r') as my_stage:
            return my_stage.read()

    def setCode(self, d=dict):
        self._code  = self.readStager()
        self._code = self._code.format(**d)

    def getCode(self):
        return self._code