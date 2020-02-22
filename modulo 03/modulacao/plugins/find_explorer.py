from plugins.plugin import Template



class findExplorer(Template):
    def __init__(self,socket):
        self.name   = 'Find Exmplorer'
        self.version    = '1.1'
        self.description = 'get all notepad file in os'
        self.payload = 'Get-Command Notepad -All | Format-Table CommandType, Name, Definition '
        self.socket  = socket
        self.targets = ['windows 10']

    def run(self):
        self.sendPayload()
