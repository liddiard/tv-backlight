from machine import PWM
from machine import Pin

pin15 = Pin(15, Pin.OUT)

pwm = PWM(pin15, freq=50, duty_u16=8192)  # create a PWM object on a pin
                                        # and set freq and duty
pwm.duty_u16(32768)     # set duty to 50%

# reinitialise with a period of 200us, duty of 5us
pwm.init(freq=5000, duty_ns=5000)

pwm.duty_ns(3000)       # set pulse width to 3us

pwm.deinit()



""" from machine import PWM 
from machine import Pin
import time


# p15 = machine.Pin(15)
p15 = Pin(15, Pin.OUT)

pwm15 = PWM(p15)

pwm15.freq(500)
pwm15.duty_u16(512)

pone5 = PWM(15, freq=50, duty_u16=8192)
time.sleep(.5)
pone5 = PWM(15, freq=50, duty_u16=2000)
time.sleep(.5)
"""

