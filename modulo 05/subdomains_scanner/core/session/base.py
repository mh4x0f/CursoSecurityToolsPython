import requests

class SessionBaseModel(object):
    def __init__(self, url_parser, token, domain, verbose=True):
        self.init_session()
        self.timeout = 25
        self.token = token
        self.domain = domain
        self.url_parser = url_parser
        self.verbose = verbose

    def init_session(self):
        self.session = requests.Session()
        self.headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Language': 'en-US,en;q=0.8',
              'Accept-Encoding': 'gzip'}


    def send_request(self, data):
        url = self.url_parser.format(**data)
        try:
            resp = self.session.get(url , headers=self.headers, timeout= self.timeout)
        except Exception:
            resp = None
        return self.get_response(resp)

    def get_response(self, response):
        if response is None:
            return 0
        return response.json()
