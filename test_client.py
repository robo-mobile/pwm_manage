#!/usr/bin/env python3

# WS client example

import asyncio
import websockets
import time
import socket

host = "127.0.0.1"
port = 5685

try:
    scan = socket.socket()
    scan.connect((host, port))
except :
    print(f"Port  -- {port} -- [CLOSED]\n")
    exit (1)
else:
    print(f"Port -- {port} -- [OPEN]")
    print(f"TEST [START]\n")

list_range = ['[1,1]', '[0,0]', '[1,0]', '[0,1]', '[0.1,0]', '[0,0.1]',
              '[1,-1]', '[-1,-1]', '[-1,1]', '[-1,0]', '[0,-1]']

async def hello():
    uri = f"ws://{host}:{port}"
    for i in list_range:
        async with websockets.connect(uri) as websocket:
            await websocket.send(i)
            time.sleep (5)

asyncio.get_event_loop().run_until_complete(hello())
print(f"TEST [END]\n")