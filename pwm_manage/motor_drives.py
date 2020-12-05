import RPi.GPIO as GPIO


class driver:
    logger: object
    channels: dict

    def __init__(self):
        for key, value in self.channels.items():
            setattr(self, key, value)

class L9110S(driver):
    # channel1 = 35
    # channel2 = 36
    # channel3 = 37
    # channel4 = 38

    def __init__(self):

        super().__init__()
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
    # enA = 33
    # in1 = 35
    # in2 = 36
    #
    # enB = 37
    # in3 = 38
    # in4 = 40

    def __init__(self):

        super().__init__()
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
    """Колеса Илона"""

    # enA1 = 40
    # in11 = 38
    # in12 = 36
    #
    # enB1 = 33
    # in13 = 35
    # in14 = 37
    #
    # enA2 = 32
    # in21 = 31
    # in22 = 29
    #
    # enB2 = 26
    # in23 = 27
    # in24 = 28


    def __init__(self, *args, **kwargs):
        super().__init__()

        print("init class")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.enA1, GPIO.OUT)
        GPIO.setup(self.enB1, GPIO.OUT)
        GPIO.setup(self.in11, GPIO.OUT)
        GPIO.setup(self.in12, GPIO.OUT)
        GPIO.setup(self.in13, GPIO.OUT)
        GPIO.setup(self.in14, GPIO.OUT)

        GPIO.setup(self.enA2, GPIO.OUT)
        GPIO.setup(self.enB2, GPIO.OUT)
        GPIO.setup(self.in21, GPIO.OUT)
        GPIO.setup(self.in22, GPIO.OUT)
        GPIO.setup(self.in23, GPIO.OUT)
        GPIO.setup(self.in24, GPIO.OUT)

        GPIO.output(self.in11, GPIO.LOW)
        GPIO.output(self.in12, GPIO.LOW)
        GPIO.output(self.in13, GPIO.LOW)
        GPIO.output(self.in14, GPIO.LOW)

        GPIO.output(self.in21, GPIO.LOW)
        GPIO.output(self.in22, GPIO.LOW)
        GPIO.output(self.in23, GPIO.LOW)
        GPIO.output(self.in24, GPIO.LOW)

        self.pwm_enA1 = GPIO.PWM(self.enA1, 1000)
        self.pwm_enB1 = GPIO.PWM(self.enB1, 1000)

        self.pwm_enA2 = GPIO.PWM(self.enA2, 1000)
        self.pwm_enB2 = GPIO.PWM(self.enB2, 1000)

        self.pwm_enA1.stop()
        self.pwm_enB1.stop()
        self.pwm_enA2.stop()
        self.pwm_enB2.stop()

    def pwm_controller(self, manage_list: list):
        a_left, a_right, b_left, b_right = manage_list
        a_left = int(a_left * 100)
        a_right = int(a_right * 100)
        b_left = int(b_left * 100)
        b_right = int(b_right * 100)
        self.logger.debug(f'a_left : {a_left}, a_right : {a_right}, b_left : {b_left}, b_right : {b_right}')

        if a_left >= 0 and a_right >= 0 and b_left >= 0 and b_right >= 0:
            """
            Приямо вперед 
            """

            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.HIGH)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.HIGH)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.HIGH)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.HIGH)
            GPIO.output(self.in24, GPIO.LOW)



        elif a_left < 0 and a_right < 0 and b_left < 0 and b_right < 0:
            """
            Приямо назад
            """

            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.HIGH)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.HIGH)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.HIGH)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.HIGH)

        elif a_left > 0 and a_right < 0 and b_left > 0 and b_right < 0:
            """
            По кругу вправо
            """

            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.HIGH)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.HIGH)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.HIGH)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.HIGH)

        elif a_left < 0 and a_right > 0 and b_left < 0 and b_right > 0:
            """
            По кругу налево
            """



            self.pwm_enA1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.HIGH)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enB1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.HIGH)

            self.pwm_enA2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.HIGH)
            GPIO.output(self.in24, GPIO.LOW)

            self.pwm_enB2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.HIGH)

        elif a_left > 0 and a_right == 0 and b_left == 0 and b_right > 0:
            """
            Наискось вперед направо
            """
            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.HIGH)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.HIGH)
            GPIO.output(self.in24, GPIO.LOW)


        elif a_left == 0 and a_right < 0 and b_left < 0 and b_right == 0:
            """
            Наискось назад направо
            """
            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.HIGH)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.HIGH)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.LOW)

        elif a_left == 0 and a_right > 0 and b_left > 0 and b_right == 0:
            """
            Наискось вперед направо
            """
            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.HIGH)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.HIGH)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.LOW)

        elif a_left < 0 and a_right == 0 and b_left == 0 and b_right < 0:
            """
            Наискось назад направо
            """
            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.HIGH)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.HIGH)

        elif a_left > 0 and a_right < 0 and b_left < 0 and b_right > 0:
            """
            В бок направо
            """
            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.HIGH)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.HIGH)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.HIGH)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.HIGH)
            GPIO.output(self.in24, GPIO.LOW)

        elif a_left < 0 and a_right > 0 and b_left > 0 and b_right < 0:
            """
            В бок налево
            """
            self.pwm_enA1.start(abs(a_left))
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.HIGH)

            self.pwm_enB1.start(abs(a_right))
            GPIO.output(self.in13, GPIO.HIGH)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enA2.start(abs(b_left))
            GPIO.output(self.in21, GPIO.HIGH)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.start(abs(b_right))
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.HIGH)

        elif a_left == 0 and a_right == 0 and b_left == 0 and b_right == 0:
            """
            STOP
            """

            self.pwm_enA1.stop()
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.stop()
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enA2.stop()
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.stop()
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.LOW)

        else:
            self.logger.error(f'Wrong data...')
            self.pwm_enA1.stop()
            GPIO.output(self.in11, GPIO.LOW)
            GPIO.output(self.in12, GPIO.LOW)

            self.pwm_enB1.stop()
            GPIO.output(self.in13, GPIO.LOW)
            GPIO.output(self.in14, GPIO.LOW)

            self.pwm_enA2.stop()
            GPIO.output(self.in21, GPIO.LOW)
            GPIO.output(self.in22, GPIO.LOW)

            self.pwm_enB2.stop()
            GPIO.output(self.in23, GPIO.LOW)
            GPIO.output(self.in24, GPIO.LOW)
