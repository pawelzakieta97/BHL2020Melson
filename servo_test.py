import pwm_controls as pwm
import time

servo = pwm.ServoMotorControls(2, 12, 50)

while True:
    servo.set_angle(0)
    time.sleep(0.5)
    servo.set_angle(90)
    time.sleep(0.5)
    servo.set_angle(180)
    time.sleep(0.5)
    servo.set_angle(90)
    time.sleep(0.5)