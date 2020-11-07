import RPi.GPIO as GPIO
from pwm_controls import DcMotorControls
from enkoder import Enkoder
import time

silnik = DcMotorControls()
enkoder = Enkoder(silnik)

while True:
    print(enkoder.get_cnt())
    time.sleep(1)