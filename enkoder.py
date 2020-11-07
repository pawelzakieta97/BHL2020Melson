import RPi.GPIO as GPIO
import time


class Enkoder:

    def __init__(self, silnik):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(5, GPIO.IN)
        self.silnik = silnik
        self.cnt = 0
        GPIO.add_event_detect(5, GPIO.RISING, callback=self.rotation_decode, bouncetime=250)

    def rotation_decode(self, pin):
        if self.silnik.is_to_front():
            self.cnt += 1
        else:
            self.cnt -= 1

    def get_cnt(self):
        return self.cnt