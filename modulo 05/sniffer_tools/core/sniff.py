from threading import Thread
import queue
from scapy.all import *
import netifaces
from plugins import *
from config.config import Settings
import sys

class Sniffer(Thread):
    def __init__(self, options):
        super(Sniffer, self).__init__()
        self.parser_options = options
        self.plugins = {}
        self._status = False
        self._interface = self.parser_options.interface
        self._filter = self.parser_options.filter
        self.config = Settings()

    def checkIface (self, iface):
        if (iface in netifaces.interfaces()):
            return True
        return False

    def getStatus(self):
        return self._status

    def setInterface(self, iface):
        self.config.setValue("interface", iface)
        self._interface = iface

    def getInterface(self):
        return self._interface

    def setStatus(self, status ):
        self._status = status

    def getStringFilter(self):
        return self._filter

    def setStringfilter(self, value):
        self._filter = value

    def exit_no_ifacesfound(self):
        print('[!] interface not found!')
        sys.exit(0)

    def sniffer(self, q):
        while not self.getStatus():
            try:
                sniff(iface=self.getInterface(), filter=self.getStringFilter(), 
                prn= lambda x: q.put(x) , store=0)
            except Exception:
                pass
            if self.getStatus():
                break

    def run(self):
        if not self.checkIface(self.getInterface()):
            return self.exit_no_ifacesfound()
        
        self.all_plugins = base.BasePlugin.__subclasses__()
        for p in self.all_plugins:
            print('[-] plugin:: {} ativo '.format(p.getName()))
            self.plugins[p.getName()] = p()
            self.plugins[p.getName()].setActivated(True)

        
        q = queue.Queue()
        
        sniff = Thread(target=self.sniffer,  args=(q,))
        sniff.deamon = True
        sniff.start()

        self.setStatus(False)
        while not self.getStatus():
            try:
                pkt = q.get(timeout=1)
                for plugin in list(self.plugins.keys()):
                    if self.plugins[plugin].getActivated():
                        self.plugins[plugin].ParserPackets(pkt)
            except queue.Empty:
                pass

    def stop(self):
        self.setStatus(True)
