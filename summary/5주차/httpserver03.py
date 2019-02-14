from http.server import CGIHTTPRequestHandler, HTTPServer
PORT = 8000
Handler = CGIHTTPRequestHandler
httpd = HTTPServer(('', PORT), Handler)

print('listening on port', PORT)
httpd.serve_forever()