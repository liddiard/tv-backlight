# inspiration from multiple sites, but started with https://www.youngwonks.com/blog/How-to-use-an-RGB-LED-with-the-Raspberry-Pi-Pico
# Needed to invert the outputs since it is an common anode LED
# the button pushes were unpredictible, so all re-written with Bill 
from machine import Pin, Signal
import time

led_r = Pin(15, Pin.OUT, Pin.PULL_UP)     # tried pull-up for red, since it is always "on" slightly.  Did not help
led_g = Pin(17, Pin.OUT)
led_b = Pin(16, Pin.OUT)
switch = Pin(0, Pin.IN, Pin.PULL_DOWN)

def redLedOn():                                     # assign red LED On
  led_r.value(0)                                    
def redLedOff():                                    # assign rel LED Off
  led_r.value(1)
def greenLedOn():                                   # assign green LED On
  led_g.value(0)
def greenLedOff():                                  # assign green LED Off
  led_g.value(1)
def blueLedOn():                                    # assign Blue LED On
  led_b.value(0)
def blueLedOff():                                   # assign Blue LED Off
  led_b.value(1)

def deBounce():
  # time.sleep(.2)
  print("debouncing")
  debounced = False
  count = 0
  limit = 2000
  while debounced == False:
    if switch.value() == 1:
        count +=1
    else:
        count = 0
    if count >= limit:
        debounced = True
        print("leaving debounce")
        

def waitForRel():
   while switch.value() == 1:
   	pass
    
def waitForSw():
   while switch.value() == 0:
    pass

#redLedOff()
#greenLedOff()
#blueLedOff()
time.sleep(.5)

while True: 
  blueLedOff()                 
  greenLedOff()
  redLedOn()					# red on
  deBounce()
  waitForRel() 
  waitForSw()
  redLedOff()

  redLedOff()
  greenLedOn()					# green on
  blueLedOff()
  deBounce()
  waitForRel()
  waitForSw()
  greenLedOff()

  redLedOff()						
  greenLedOff()
  blueLedOn()					# blue on
  deBounce()
  waitForRel()
  waitForSw()
  blueLedOff()
  
  redLedOff()					# turquoise (blue+green)
  greenLedOn()
  blueLedOn()
  deBounce()
  waitForRel()
  waitForSw()
  greenLedOff()
  blueLedOff()

  redLedOn()					# purple (red+blue)
  greenLedOff()
  blueLedOn()
  deBounce()
  waitForRel()
  waitForSw()
  redLedOff()
  blueLedOff()

  redLedOn()					# orange (red+green)
  greenLedOn()
  blueLedOff()
  deBounce()
  waitForRel()
  waitForSw()
  redLedOff()
  greenLedOff()

  redLedOff()					# all off
  greenLedOff()
  blueLedOff()
  deBounce()
  waitForRel()
  waitForSw()



 
 
  
