from payloads.base import BasePayload
from core.common.config import Settings


class Basic(BasePayload):
    _name  = "Basic"
    _code = None
    _activated = False
    _conf = Settings() 
    _stager_path = "stagers/basic.ps1"

    @staticmethod
    def getName():
        return Basic._name

    def __init__(self):
        self.setActivated(self._conf.getPayloadStatus(self._name))