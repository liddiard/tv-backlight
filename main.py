# inspration from multiple sites, but started with https://www.youngwonks.com/blog/How-to-use-an-RGB-LED-with-the-Raspberry-Pi-Pico
# Needed to invert the outputs since it is an common anode LED

from machine import Pin, Signal
import time

led_r = Signal(15, Pin.OUT, invert=True)            # need to invert the ouptut due to using anode LED         
led_g = Signal(17, Pin.OUT, invert=True)            # need to invert the ouptut due to using anode LED
led_b = Signal(16, Pin.OUT, invert=True)            # need to invert the ouptut due to using anode LED
switch = Pin(0, Pin.IN, Pin.PULL_DOWN)

def redLedOn():                                     # assign red LED On
  led_r.on()                                    
def redLedOff():                                    # assign rel LED Off
  led_r.off()
def greenLedOn():                                   # assign green LED On
  led_g.on()
def greenLedOff():                                  # assign green LED Off
  led_g.off()
def blueLedOn():                                    # assign Blue LED On
  led_b.on()
def blueLedOff():                                   # assign Blue LED Off
  led_b.off()

redLedOff()
greenLedOff()
blueLedOff()
#time.sleep(.2)

while True:                      # red only
  while(switch.value()==0):
    redLedOn()
    time.sleep(.2)               # to help with debounce

  redLedOff()

  while(switch.value()==0):     # green only
    greenLedOn()
    time.sleep(.2)

  greenLedOff()

  while(switch.value()==0):     # blue only
    blueLedOn()
    time.sleep(.2)

  blueLedOff()

  while(switch.value()==0):     # blue and green
    blueLedOn()
    greenLedOn()
    time.sleep(.2)

  greenLedOff()
  blueLedOff()

  while(switch.value()==0):     # blue and green
    redLedOn()
    greenLedOn()
    time.sleep(.2)

  redLedOff()
  greenLedOff()
#  blueLedOff()

# the routine seems to cause it to skip the red while loop at the first
#  while(switch.value()==0):
#    print(" ")
#    time.sleep(.2)

 
 
  
