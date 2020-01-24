from core.runtimes.thread import enumratorBaseThreaded
import threading
from tabulate import tabulate



class Spyse(enumratorBaseThreaded):
    url_parser = "https://api.spyse.com/v1/subdomains?api_token={TOKEN}&domain={DOMAIN}&page={PAGEID}"
    engine_name = "Spyse"
    description = " new search engine for scan subdomains"
    type_scanner = "subdomains"

    @staticmethod
    def getEngineName():
        return Spyse.engine_name


    def __init__(self, domain, token, q=None, verbose=True):
        self.threads = 70
        self.token = token
        self.q = q
        self.domain = domain
        self.lock = threading.BoundedSemaphore(value=self.threads)
        super(Spyse, self).__init__(self.url_parser, self.engine_name
        ,self.domain, self.token, q=self.q, verbose=verbose)

    
    def print_data(self, data):
        hearders = ['Subdomains', "IP"]
        table = []
        for i in range(0, data["count"]):
            if (type(data["records"][i]['ip']) != list):
                table.append([data["records"][i]["domain"], data["records"][i]["ip"]["ip"]])
            else:
                table.append([data["records"][i]["domain"], "not found"])
        print(tabulate(table, hearders, tablefmt="psql"))


    def enumarate(self):
        self.lock.acquire()
        data_content = self.send_request({'TOKEN': self.token, 'DOMAIN': self.domain,
                                        'PAGEID' : 1})
        print(self.print_data(data_content))
        return data_content
