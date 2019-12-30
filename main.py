#!/usr/bin/env python3

import asyncio
import websockets
import json
import RPi.GPIO as GPIO
import time

led1 = 3
led2 = 5
led3 = 7
switch = 31


def myGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)

    GPIO.setup(switch, GPIO.IN)

    for i in range(1000):
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led1, GPIO.LOW)
        time.sleep(0.2)

        GPIO.output(led2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led2, GPIO.LOW)
        time.sleep(0.2)

        GPIO.output(led3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led3, GPIO.LOW)
        time.sleep(0.2)

        print('Switch status = ', GPIO.input(switch))

    GPIO.cleanup()


async def hello(websocket, path):
    jsonCommand = await websocket.recv()
    print(f"< {jsonCommand}")
    output_list = json.loads()

    # greeting = f"Hello {name}!"
    #
    # await websocket.send(greeting)
    # print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()





