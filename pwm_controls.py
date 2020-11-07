import RPi.GPIO as GPIO


class DcMotorControls:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        self.p1 = GPIO.PWM(8, 100)
        self.p2 = GPIO.PWM(10, 100)
        self.p1.start(0)
        self.p2.start(0)
        self.front = True

    def set_speed(self, speed):
        if speed >= 0:
            self.p2.ChangeDutyCycle(0)
            self.p1.ChangeDutyCycle(speed / 2)
            self.front = True
        else:
            self.p1.ChangeDutyCycle(0)
            self.p2.ChangeDutyCycle(- speed / 2)
            self.front = False

    def is_to_front(self):
        return self.front


class ServoMotorControls:

    def __init__(self, low, high, freq):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        self.p = GPIO.PWM(3, freq)
        self.p.start(0)
        self.min = low
        self.max = high

    def set_angle(self, angle):
        duty = self.min + ((self.max - self.min) * angle / 180)
        self.p.ChangeDutyCycle(duty)

# LED  = 1 # gpio pin 12 = wiringpi no. 1 (BCM 18)
#
# # Initialize PWM output for LED
# wiringpi.wiringPiSetup()
# wiringpi.pinMode(LED, 2)     # PWM mode
# wiringpi.pwmWrite(LED, 0)    # OFF
#
# while True:
#     wiringpi.pwmWrite(LED, 50)
#     time.sleep(0.5)
#     #wiringpi.pwmWrite(LED, 0)
#     time.sleep(0.5)
#
# # Set LED brightness
# def led(led_value):
#     wiringpi.pwmWrite(LED,led_value)