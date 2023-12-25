# adapted from https://www.youngwonks.com/blog/How-to-use-an-RGB-LED-with-the-Raspberry-Pi-Pico
# Initially this sketch did not work. I finally figured out I needed to switch "on" and "off" since it is a common anode, thus off is on :)

from machine import Pin
import time
# test comment

led_r = Pin(15, Pin.OUT)
led_g = Pin(17, Pin.OUT)
led_b = Pin(16, Pin.OUT)

while True:
  # led_r.off()              # turn RED led on   YES, on is off, off is on due to common ANODE led
  led_g.off()              # turn GREEN led off
  led_b.off()              # turn BLUE led off
  time.sleep(3)

  led_r.off()
  led_g.off()
  time.sleep(2)
  led_r.on()
  led_g.on()
  time.sleep(.5)

  #led_r.off()
  led_b.off()
  time.sleep(2)
  #led_r.on()
  led_b.on()
  time.sleep(.5)
  
  led_b.off()
  led_g.off()
  time.sleep(2)
  led_b.on()
  led_g.on()
  time.sleep(2)
  
  
"""  
  led_r.toggle()
    time.sleep(1)
    led_r.toggle()
    
    led_g.toggle()
    time.sleep(1)
    led_g.toggle()

    led_b.toggle()
    time.sleep(1)
    led_b.toggle()

"""
