#!/usr/bin/python3

import json
import socket
import config

def get():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(config.fastd_sock_path)

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

    yield 'peer_count', online, { 'online': 'true' }
    yield 'peer_count', offline, { 'online': 'false' }

name = 'fastd'
