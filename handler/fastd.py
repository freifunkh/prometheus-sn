#!/usr/bin/python

import sys
import json
import socket

socket_path = sys.argv[1]
socket_name = sys.argv[2] if len(sys.argv) > 2 else None

def format_output(name, attrs, value):
    if socket_name is not None:
        attrs['name'] = socket_name

    ret = [ k + '="' + v + '"' for k, v in attrs.items() ]

    return name + '{' + ','.join(ret) + '} ' + str(value)


def get():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(socket_path)

    res = bytes()
    while True:
        r = client.recv(1024)
        if not r:
            break
        res += r

    return json.loads(res.decode('utf-8'))


def status():
    json_res = get()
    peers = json_res['peers'].values()

    online = len(list(filter(lambda p: p['connection'] is not None, peers)))
    offline = len(peers) - online

    print(format_output('fastd_peer_count', dict(online='true'), online))
    print(format_output('fastd_peer_count', dict(online='false'), offline))


if __name__ == '__main__':
    status()
