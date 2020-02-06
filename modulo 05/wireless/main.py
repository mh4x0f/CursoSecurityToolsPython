from threading import Thread
import queue
from scapy.all import *
import random,os, time
from multiprocessing import Process
import netifaces
from tabulate import tabulate


interface = "wlxc83a35cef744"

def channel_hopper():
    while True:
        try:
            channel = random.randrange(1, 11)
            os.system("iw dev %s set channel %d" %(interface, channel))
        except KeyboardInterrupt:
            break

class snifferWireless(object):
    def __init__(self, options):
        self.parser_options = options
        self._status = {}
        self.output = []
        self.headers = ['Channel', 'BSSID', 'SSID']

    def checkIface(self, iface):
        if ( iface in netifaces.interfaces()):
            return True
        return False

    def getStatus(self):
        return self._status

    def setStatus(self, flag):
        self._status = flag

    def callBackPackets(self, pkt):
        if (pkt.haslayer(Dot11Beacon)):
            ssid = pkt[Dot11Elt].info
            bssid = pkt[Dot11].addr3
            channel = int(ord(pkt[Dot11Elt:3].info))
            self.output.append([channel, bssid, ssid])
            os.system("clear")
            print(tabulate(self.output, self.headers, tablefmt="simple"))

    def main(self):
        if not self.checkIface(self.parser_options):
            exit("[!] the interface not found!")

        p = Process(target=channel_hopper)
        p.start()
        
        sniff(iface="wlxc83a35cef744", prn=self.callBackPackets)


teste  = snifferWireless("wlxc83a35cef744")
teste.main()