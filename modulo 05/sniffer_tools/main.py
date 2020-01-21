
from core.console import Console
import argparse
import signal


if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="sniff tool packet on the fly")
    parser.add_argument('-i','--interface', dest='interface', help='set the interface to sniff', default=None)
    parser.add_argument('-f','--filter', dest='filter', help='set the string filter to sniff', default='tcp and ( port 80)')
    parser.add_argument('-v','--version', dest='version', help='show version the tool')

    console = Console(parser.parse_args())
    console.cmdloop("sniff tool packet on the fly")
    #signal.signal(signal.SIGINT, signal_handler)
    #sniffer.run()
    signal.pause()