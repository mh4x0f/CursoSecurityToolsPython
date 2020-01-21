
from scapy.all import hexdump

class BasePlugin(object):
    name = 'plugin master'
    version = '1.0'

    def ParserPackets(self, pkt):
        raise NoImplementedError

    def hexdumpPacket(self, pkt):
        return hexdump(pkt)