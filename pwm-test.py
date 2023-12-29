import time
from machine import PWM, Pin 

p15 = Pin(15, Pin.OUT)
p16 = Pin(16, Pin.OUT)
p17 = Pin(17, Pin.OUT)

pwm15 = PWM(p15, freq=50, duty_u16=8192)  # create a PWM object on a pin

while True: 
    for duty in range(0, 65535):
        pwm15.duty_u16(duty) # For ESP32
        time.sleep(.00099)

