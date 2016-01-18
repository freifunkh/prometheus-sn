#!/usr/bin/python3

import json
import http.server

def format_attrs(attrs):
    ret = [ k + '="' + v + '"' for k, v in attrs.items() ]

    return '{' + ','.join(ret) + '}'
    
    

def handle_request():
    with open('/tmp/prometheus-source.jsons') as f:
        for line in f:
            j = json.loads(line)

            name = j['name']
            value = j['value']

            del j['name']
            del j['value']

            yield name + format_attrs(j) + ' ' + str(value)

    
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        result = ""
        try:
            for line in handle_request():
                result += line + '\n'

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
