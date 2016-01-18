#!/usr/bin/python3

import config
import http.server

import status_fastd

modules = [
    status_fastd
]

def format_attrs(attrs):
    ret = [ k + '="' + v + '"' for k, v in attrs.items() ]

    return '{' + ','.join(ret) + '}'
    
    

def handle_request():
    for module in modules:

        for key, value, attrs in module.status():
            attrs = attrs.copy()
            attrs.update({ 'hostname': config.hostname })
            yield module.name + '_' + key + format_attrs(attrs) + ' ' + str(value)


class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        for line in handle_request():
            self.wfile.write(line.encode('utf-8') + b'\n')

server = http.server.HTTPServer(('', config.port), Handler)
server.serve_forever()
