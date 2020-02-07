
from threading import Thread
import queue
from scapy.all import *
import netifaces
from tabulate import tabulate
import random, os, time
from multiprocessing import Process


def channel_hopper():
    while True:
        try:
            channel = random.randrange(1,15)
            os.system("iw dev %s set channel %d" % ("wlxc83a35cef744", channel))
            time.sleep(1)
        except KeyboardInterrupt:
            break

class sniffer(object):
    def __init__(self, options):
        self.parser_options = options
        self.plugins = {}
        self._status = False
        self._filter = self.parser_options
        self.output = []
        self.headers = ['Channel', 'BSSID', 'SSID']

    def run(self):
        pass
    
    def checkIface(self, iface):
        if (iface in netifaces.interfaces()):
            return True
        return False
    
    def getStatus(self):
        return self._status
    
    def setStatus(self, status):
        self._status = status

    def getStringFilter(self):
        return self._filter
    
    def setStringFilter(self, value):
        self._filter = value


    def callBackPackets(self, pkt):
        if ( pkt.haslayer(Dot11Beacon)):
            ssid       = pkt[Dot11Elt].info
            bssid      = pkt[Dot11].addr3    
            channel    = int( ord(pkt[Dot11Elt:3].info))
            #print("{} {}  {} {}".format(int(channel), enc, bssid, ssid))
            self.output.append([channel, bssid, ssid]) 
            os.system("clear")
            print(tabulate(self.output, self.headers, tablefmt="simple"))


    def main(self):

        if not self.checkIface(self.parser_options):
            return
        
        p = Process(target = channel_hopper)
        p.start()

        sniff(iface="wlxc83a35cef744",prn =self.callBackPackets)

teste =  sniffer("wlxc83a35cef744")
teste.main()
