#!/usr/bin/env python3

# WS client example

import asyncio
import websockets
import time


list_range = ['[1,1]', '[0,0]', '[1,0]', '[0,1]', '[0.1,0]', '[0,0.1]']

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = '[0.1, 1]'

        await websocket.send(name)
            # print (speed)
        time.sleep (1)
        await websocket.send(name)

        # print(f"> {name}")
        # print(f"> {name}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
