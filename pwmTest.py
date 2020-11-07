import pwm_controls as pwm
import time

#servo = pwm.ServoMotorControls(5, 10, 50)
dc = pwm.DcMotorControls()

while True:
    time.sleep(1)
    dc.set_speed(100)
    time.sleep(1)
    dc.set_speed(50)
    time.sleep(1)
    dc.set_speed(-50)
    time.sleep(1)
    dc.set_speed(-100)
    time.sleep(1)
    dc.set_speed(-50)
    time.sleep(1)
    dc.set_speed(50)
