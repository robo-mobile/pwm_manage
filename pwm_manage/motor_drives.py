import RPi.GPIO as GPIO



class driver():
    logger: object
    channels: dict


class StandartPWM(driver):

    channel1 = 35
    channel2 = 36
    channel3 = 37
    channel4 = 38

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

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

    def pwm_controller(self, manage_list):
        left, right = manage_list
        left = int(left * 100)
        right = int(right * 100)
        self.logger.debug(f'left : {left}')
        self.logger.debug(f'right : {right}')

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


class L298N(driver):
    enA = 33
    in1 = 35
    in2 = 36

    enB = 37
    in3 = 38
    in4 = 40

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

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

    def pwm_controller(self, manage_list: list):
        left, right = manage_list
        left = int(left * 100)
        right = int(right * 100)
        self.logger.debug(f'left : {left}')
        self.logger.debug(f'right : {right}')

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


class DL298N(driver):

    enA1 = 33
    in11 = 35
    in12 = 36

    enB1 = 37
    in13 = 38
    in14 = 40

    enA2 = 33
    in21 = 35
    in22 = 36

    enB2 = 37
    in23 = 38
    in24 = 40

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.logger.debug('Starting servo service!')

        GPIO.setup(self.enA1, GPIO.OUT)
        GPIO.setup(self.enB1, GPIO.OUT)
        GPIO.setup(self.in11, GPIO.OUT)
        GPIO.setup(self.in12, GPIO.OUT)
        GPIO.setup(self.in13, GPIO.OUT)
        GPIO.setup(self.in14, GPIO.OUT)

        GPIO.output(self.in11, GPIO.LOW)
        GPIO.output(self.in12, GPIO.LOW)
        GPIO.output(self.in13, GPIO.LOW)
        GPIO.output(self.in14, GPIO.LOW)

        self.pwm_enA = GPIO.PWM(self.enA1, 1000)
        self.pwm_enB = GPIO.PWM(self.enB1, 1000)

        self.pwm_enA.stop()
        self.pwm_enB.stop()
