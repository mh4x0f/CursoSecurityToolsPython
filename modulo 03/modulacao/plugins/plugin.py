



class Template(object):
    name    = 'plugin master'
    version = '1.0'
    description = 'this is a plugins demo'
    payload = None
    socket  = None
    targets = []

    def checkMachine(self, os_machine):
        if os_machine in targets:
            return true
        return false

    def getPayload(self):
        return self.payload

    def sendPayload(self):
        socket.send(self.getPayload())
