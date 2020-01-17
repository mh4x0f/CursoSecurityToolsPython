from payloads.base import BasePayload
from core.common.config import Settings


class Semfuncoes(BasePayload):
    _name  = "semfuncoes"
    _code = None
    _activated = False
    _conf = Settings() 
    _stager_path = "stagers/sem_funcoes.ps1"

    @staticmethod
    def getName():
        return Semfuncoes._name

    def __init__(self):
        self.setActivated(self._conf.getPayloadStatus(self._name))