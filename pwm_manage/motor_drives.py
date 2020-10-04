import RPi.GPIO as GPIO



class driver():
    logger:object
    channels:dict


class StandartPWM(drive):
    def __init__(self):
        self.channel1 = 35
        self.channel2 = 36
        self.channel3 = 37
        self.channel4 = 38

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.logger.info('Starting servo service!')

        GPIO.setup(self.channel1, GPIO.OUT)
        GPIO.setup(self.channel2, GPIO.OUT)
        GPIO.setup(self.channel3, GPIO.OUT)
        GPIO.setup(self.channel4, GPIO.OUT)

        self.pwm_channel1 = GPIO.PWM(self.channel1, 1000)
        self.pwm_channel2 = GPIO.PWM(self.channel2, 1000)
        self.pwm_channel3 = GPIO.PWM(self.channel3, 1000)
        self.pwm_channel4 = GPIO.PWM(self.channel4, 1000)

        self.pwm_channel1.stop()
        self.pwm_channel2.stop()
        self.pwm_channel3.stop()
        self.pwm_channel4.stop()

    async def pwm_controller(self, manage_list):
        left, right = manage_list
        left = int(left * 100)
        right = int(right * 100)
        logger.info(f'left : {left}')
        logger.info(f'right : {right}')

        if left >= 0 and right >= 0:
            self.pwm_channel1.start(abs(left))
            self.pwm_channel2.stop()
            self.pwm_channel3.start(abs(right))
            self.pwm_channel4.stop()

        elif left < 0 and right < 0:

            self.pwm_channel1.stop()
            self.pwm_channel2.start(abs(left))
            self.pwm_channel3.stop()
            self.pwm_channel4.start(abs(right))

        elif left >= 0 and right < 0:

            self.pwm_channel1.start(abs(left))
            self.pwm_channel2.stop()
            self.pwm_channel3.stop()
            self.pwm_channel4.start(abs(right))

        elif left < 0 and right >= 0:

            self.pwm_channel1.stop()
            self.pwm_channel2.start(abs(left))
            self.pwm_channel3.start(abs(right))
            self.pwm_channel4.stop()

        elif left == 0 and right == 0:

            self.pwm_channel1.stop()
            self.pwm_channel2.stop()
            self.pwm_channel3.stop()
            self.pwm_channel4.stop()

class L298 (driver):

    def __init__(self):
        self.enA = 33
        self.in1 = 35
        self.in2 = 36

        self.enB = 37
        self.in3 = 38
        self.in4 = 40


        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.logger.info('Starting servo service!')

        GPIO.setup(self.enA, GPIO.OUT)
        GPIO.setup(self.enB, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)

        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

        self.pwm_enA = GPIO.PWM(self.enA, 1000)
        self.pwm_enB = GPIO.PWM(self.enB, 1000)

        self.pwm_enA.stop()
        self.pwm_enB.stop()

    def pwm_controller(self, manage_list):
        left, right = manage_list
        left = int(left * 100)
        right = int(right * 100)
        self.logger.info(f'left : {left}')
        self.logger.info(f'right : {right}')

        if left >= 0 and right >= 0:

            self.pwm_enA.start(abs(left))
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)

            self.pwm_enB.start(abs(right))
            GPIO.output(self.in3, GPIO.HIGH)
            GPIO.output(self.in4, GPIO.LOW)


        elif left < 0 and right < 0:

            self.pwm_enA.start(abs(left))
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)

            self.pwm_enB.start(abs(right))
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.HIGH)

        elif left >= 0 and right < 0:

            self.pwm_enA.start(abs(left))
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)

            self.pwm_enB.start(abs(right))
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.HIGH)

        elif left < 0 and right >= 0:

            self.pwm_enA.start(abs(left))
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)

            self.pwm_enB.start(abs(right))
            GPIO.output(self.in3, GPIO.HIGH)
            GPIO.output(self.in4, GPIO.LOW)

        elif left == 0 and right == 0:

            self.pwm_enA.stop()
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)

            self.pwm_enB.stop()
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.LOW)

class double_l298n (driver):
    pass

