#!/usr/bin/env python3

import asyncio
import websockets
import json
import RPi.GPIO as GPIO
import time

import logging
import random
import time
from systemd.journal import JournaldLogHandler

logger = logging.getLogger("pwm_manage")

# instantiate the JournaldLogHandler to hook into systemd
journald_handler = JournaldLogHandler()

# set a formatter to include the level name
journald_handler.setFormatter(logging.Formatter(
    '[%(levelname)s] %(message)s'
))

# add the journald handler to the current logger
logger.addHandler(journald_handler)

# optionally set the logging level
logger.setLevel(logging.DEBUG)

channel1 = 35
channel2 = 36
channel3 = 37
channel4 = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
logger.info('Starting servo service!')

GPIO.setup(channel1, GPIO.OUT)
GPIO.setup(channel2, GPIO.OUT)
GPIO.setup(channel3, GPIO.OUT)
GPIO.setup(channel4, GPIO.OUT)

pwm_channel1 = GPIO.PWM(channel1, 1000)
pwm_channel2 = GPIO.PWM(channel2, 1000)
pwm_channel3 = GPIO.PWM(channel3, 1000)
pwm_channel4 = GPIO.PWM(channel4, 1000)

pwm_channel1.stop()
pwm_channel2.stop()
pwm_channel3.stop()
pwm_channel4.stop()


def pwm_controller(manage_list):
    left, right = manage_list
    left = int(left * 100)
    right = int(right * 100)
    logger.info(f'left : {left}')
    logger.info(f'right : {right}')

    if left >= 0 and right >= 0:
        pwm_channel1.start(abs(left))
        pwm_channel2.stop()
        pwm_channel3.start(abs(right))
        pwm_channel4.stop()

        # time.sleep(1)
        # pwm.ChangeDutyCycle(80)
        # pwm.stop()  # Останавливаем ШИМ

    elif left < 0 and right < 0:

        pwm_channel1.stop()
        pwm_channel2.start(abs(left))
        pwm_channel3.stop()
        pwm_channel4.start(abs(right))

    elif left >= 0 and right < 0:

        pwm_channel1.start(abs(left))
        pwm_channel2.stop()
        pwm_channel3.stop()
        pwm_channel4.start(abs(right))

    elif left < 0 and right >= 0:

        pwm_channel1.stop()
        pwm_channel2.start(abs(left))
        pwm_channel3.start(abs(right))
        pwm_channel4.stop()

    elif left == 0 and right == 0:

        pwm_channel1.stop()
        pwm_channel2.stop()
        pwm_channel3.stop()
        pwm_channel4.stop()


async def consumer(message):
    output_list = json.loads(message)
    logger.info(f'INPUT json: {output_list}')
    pwm_controller(output_list)


async def websocket_server(websocket, path):
    async for message in websocket:
        await consumer(message)


if __name__ == '__main__':
    start_server = websockets.serve(websocket_server, "127.0.0.1", 5685)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
