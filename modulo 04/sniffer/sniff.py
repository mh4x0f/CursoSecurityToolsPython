from threading import Thread
import queue
from scapy.all import *
import netifaces
from plugins import *
import argparse
import signal
import sys

class Sniffer(object):
    def __init__(self, options):
        self.parser_options = options
        self.plugins = {}
        self._status = False
        self._filter = self.parser_options.filter

    def checkIface (self, iface):
        if (iface in netifaces.interfaces()):
            return True
        return False

    def getStatus(self):
        return self._status
    
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
                sniff(iface=self.parser_options.interface, filter=self.getStringFilter(), 
                prn= lambda x: q.put(x) , store=0)
            except Exception:
                pass
            if self.getStatus():
                break

    def run(self):
        if not self.checkIface(self.parser_options.interface):
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
    

def signal_handler(signal, frame):
    sys.exit(0)

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="sniff packet on the fly")
    parser.add_argument('-i','--interface', dest='interface', help='set the interface to sniff', default=None)
    parser.add_argument('-f','--filter', dest='filter', help='set the string filter to sniff', default='tcp and ( port 80)')
    parser.add_argument('-v','--version', dest='version', help='show version the tool')

    sniffer = Sniffer(parser.parse_args())
    signal.signal(signal.SIGINT, signal_handler)
    sniffer.run()
    signal.pause()