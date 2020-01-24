import multiprocessing
from core.session.base import SessionBaseModel



class enumratorBaseThreaded(multiprocessing.Process, SessionBaseModel):
    def __init__(self, url_parser, engine_name, domain, token, **args):
        self.verbose = args["verbose"]
        SessionBaseModel.__init__(self, url_parser, token, domain, verbose=self.verbose)
        multiprocessing.Process.__init__(self)
        self.q = args['q']

    def run(self):
        domain_list = self.enumarate()
        for domain in domain_list.keys():
            self.q.append({domain : domain_list[domain]})
