#!/usr/bin/python3

import sys
import json
import http.server

def handle_request():
    with open('/tmp/prometheus.metrics') as f:
        return f.read()

    
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        result = ""
        try:
            result = handle_request()

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(result.encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            raise e

server = http.server.HTTPServer(('', 12345), Handler)
server.serve_forever()
