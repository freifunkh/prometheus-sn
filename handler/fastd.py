#!/usr/bin/python3

import sys
import json
import socket

socket_path = sys.argv[1]

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

    yield dict(name='peer_count', value=online, online='true')
    yield dict(name='peer_count', value=offline, online='false')


for s in status():
    print(json.dumps(s))


