from pwm_controls import DcMotorControls
from pwm_controls import ServoMotorControls
from enkoder import Enkoder
import time

motor = DcMotorControls()

servo = ServoMotorControls(2, 12, 50)

kosz = 0

servo.set_angle(0)
motor.set_speed(50)
time.sleep(2)
enkoder = Enkoder(motor)

while True:
    motor.set_speed(-50)
    print(enkoder.get_cnt())
    if enkoder.get_cnt()*enkoder.get_cnt() >= 60 and kosz==0:
        motor.set_speed(0)
        time.sleep(1)
        servo.set_angle(90)
        time.sleep(1)
        servo.set_angle(0)
        time.sleep(1)
        kosz = 1

    if enkoder.get_cnt()*enkoder.get_cnt() >= 300 and kosz==1:
        motor.set_speed(0)
        time.sleep(1)
        servo.set_angle(90)
        time.sleep(1)
        servo.set_angle(0)
        time.sleep(1)
        kosz = 2

    if enkoder.get_cnt()*enkoder.get_cnt() >= 700 and kosz==2:
        motor.set_speed(0)
        time.sleep(1)
        servo.set_angle(90)
        time.sleep(1)
        servo.set_angle(0)
        time.sleep(1)
        break