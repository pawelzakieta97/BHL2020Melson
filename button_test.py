import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)

while True:
    if GPIO.input(31):
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
    elif GPIO.input(33):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
    elif GPIO.input(35):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
    elif GPIO.input(37):
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
    else:
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)