import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

while True:
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)