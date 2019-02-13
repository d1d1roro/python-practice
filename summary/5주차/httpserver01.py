from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time
PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/':
            self.send_error(404, 'File not found')
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(time.asctime())
        # stdout = sys.stdout
        # sys.stdout = self.wfile
        # self.printPage()
        # sys.stdout = stdout
    def printPage(self):
        t = time.asctime()
        # msg = b"<html><body>접속한 시각: <b>" + t + "</b></body></html>"
        # print(msg.encode())

httpd = HTTPServer(('', PORT), MyHandler)
print('listening on port', PORT)
httpd.serve_forever()