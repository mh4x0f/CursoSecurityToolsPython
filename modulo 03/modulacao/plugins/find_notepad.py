from plugins.plugin import Template



class findNotepadPath(Template):
    def __init__(self,socket):
        self.name   = 'Find Notepad'
        self.version    = '1.0'
        self.description = 'get all notepad file in os'
        self.payload = 'Get-Command Notepad -All | Format-Table CommandType, Name, Definition '
        self.socket  = socket
        self.targets = ['windows 10']

    def run(self):
        self.sendPayload()
