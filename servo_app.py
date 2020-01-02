#!/usr/bin/env python3

import asyncio
import websockets
import json
#import RPi.GPIO as GPIO
import time

import logging
import random
import time
from systemd.journal import JournaldLogHandler


logger = logging.getLogger(__name__)

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



channel1 = 3
channel2 = 5
channel3 = 7
channel4 = 8


def servoDriver(json_list):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    logger.info('Start servo')

    GPIO.setup(channel1, GPIO.OUT)
    GPIO.setup(channel2, GPIO.OUT)
    GPIO.setup(channel3, GPIO.OUT)
    GPIO.setup(channel4, GPIO.OUT)

    pwm = GPIO.PWM(channel1, 1000)  # Создаем ШИМ-объект для пина pinPWM с частотой 50 Гц

    pwm.start(50)  # Запускаем ШИМ на пине со скважностью 50% (0-100%)
    time.sleep(1)
    # Можно использовать данные типа float - 49.5, 2.45
    pwm.ChangeDutyCycle(80)  # Изменяем скважность до 80%
    time.sleep(5)
    pwm.ChangeFrequency(1000)  # Изменяем частоту до 1000 Гц (также можно float)
    pwm.stop()  # Останавливаем ШИМ

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
    # print(f"< {jsonCommand}")
    output_list = json.loads(jsonCommand)
    print (output_list)
    # greeting = f"Hello {name}!"
    #
    # await websocket.send(greeting)
    # print(f"> {greeting}")

start_server = websockets.serve(hello, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# if __name__ == '__main__':
#     pwd()