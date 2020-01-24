from modules import *
import multiprocessing
from core.runtimes.thread import enumratorBaseThreaded
import argparse
from colorama import Fore, Back, Style


def banner():
    return Fore.RED + 'SpyseTools'

version = "v1.0"

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="SpyseTool - moduled scanner from API Spyse")
    parser.add_argument('-t','--token', dest='token', help='set your api_token service', 
    default='rAaHZ_M_cSF-rq8r2xYHNtok4Y9tZEN9', required=True)
    parser.add_argument('-d','--domain', dest='domain', help='set target doamin ', required=True)
    parser.add_argument('-v','--version', dest='version', help='show version the tool')
    parser_load = parser.parse_args()

    modules = {}
    list_modules = enumratorBaseThreaded.__subclasses__()
    for m in list_modules:
        modules[m.getEngineName()] = m

    subdomains_queue = multiprocessing.Manager().list()


    domain = parser_load.domain
    token = parser_load.token
    thread = modules["Spyse"](domain, token, q=subdomains_queue, verbose=True)
    thread.start()
    thread.join()
    print(subdomains_queue)