from multiprocessing import Process, Manager
from os import devnull, popen
from threading import Thread
from subprocess import Popen, PIPE, STDOUT
from tabulate import tabulate 
import requests




class ThreadFastScanIP(Thread):

    def __init__(self, gateway, range_start, range_end, parent= None):
        super(ThreadFastScanIP, self).__init__(parent)
        self.range_start = range_start
        self.range_end = range_end
        self.working_thread = True
        self.on_ips = []
        # '192.168.174.'
        self.gatewayNT = gateway[:len(gateway) - len(gateway.split('.').pop())]

    def run(self):
        self.jobs = []
        self.manager = Manager()
        self.on_ips = self.manager.dict()
        for count in range(self.range_start, self.range_end):
            ip='%s{0}'.format(count)%(self.gatewayNT)
            if not self.working_thread: break
            p = Process(target=self.working, args=(ip, self.on_ips))
            self.jobs.append(p)
            p.start()
        
        for proc in self.jobs:
            proc.join()
            proc.terminate()
        
    def working(self, ip, lista):
        with open(devnull , 'wb') as limbo:
            result = Popen(['ping', '-c', '1', '-n' , '-W' , '1' , ip], 
            stdout=limbo, stderr=limbo).wait()
            if not result:
                if (self.get_mac(ip) == None):
                    lista[ip] = {'mac' : '',  'vendor' : ''}
                else:
                    lista[ip] = {'mac' : self.get_mac(ip),  
                    'vendor' : self.resolver_mac(self.get_mac(ip))}

    def get_mac(self, host):
        fields = popen('grep "%s" /proc/net/arp' % host).read().split()
        if len(fields) == 6  and fields[3] != '00:00:00:00:00:00':
            return fields[3]
        return None

    def resolver_mac(self,mac):
        MAC_URL = 'http://macvendors.co/api/%s'
        try:
            r =  requests.get(MAC_URL % mac.upper())
        except:
            return ''
        return r.json()['result']['company']


    def getOutput(self):
        return self.on_ips

    def showoutput_table(self):
        keys = self.on_ips.keys()
        values = self.on_ips.values()

        data = { 'IP': keys, 
                 'MAC' : [v['mac'] for v in values],
                 'VENDORS' : [v['vendor'] for v in values]}
        
        print(tabulate(data, headers='keys'))



if (__name__ == '__main__'):
    thread_scan  =  ThreadFastScanIP('192.168.174.1', 0, 255)
    thread_scan.start()
    thread_scan.join()
    #print(thread_scan.getOutput())
    print(thread_scan.showoutput_table())