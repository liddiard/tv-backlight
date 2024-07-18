# inspiration from multiple sites, but started with https://www.youngwonks.com/blog/How-to-use-an-RGB-LED-with-the-Raspberry-Pi-Pico
# Needed to invert the outputs since it is an common anode LED
# the button pushes were unpredictible, so pretty much all re-written with Bill.  I suck :( 
# Many modes.  Bill figured out it will work if I totally remove the resistor (which the leaves no current limiting)
# July 15, 2024: uploaded to the pico, and put it in a box.  Seems to work, but will skip sometimes. No problem.

from machine import Pin
from time import sleep_ms

led_r = Pin(18, Pin.OUT, Pin.PULL_UP)     # for some current limiting, put a 22 ohm resistor from the anode to 3.3v rail
led_g = Pin(19, Pin.OUT)
led_b = Pin(20, Pin.OUT)
switch = Pin(27, Pin.IN, Pin.PULL_DOWN)

def redLedOn():                           # assign red LED On
  led_r.value(0)                                    
def redLedOff():                          # assign rel LED Off
  led_r.value(1)
def greenLedOn():                         # assign green LED On
  led_g.value(0)
def greenLedOff():                        # assign green LED Off
  led_g.value(1)
def blueLedOn():                          # assign Blue LED On
  led_b.value(0)
def blueLedOff():                         # assign Blue LED Off
  led_b.value(1)

def deBounce():                           # debounce switch
  print("debouncing")
  debounced = False
  count = 0
  limit = 2000
  sleep_ms(100)
  while debounced == False:
    if switch.value() == 1:
        count +=1
    else:
        count = 0
    if count >= limit:
        debounced = True
        print("leaving debounce")
        

def waitForRel():                         # checks if the switch has been released
   while switch.value() == 1:
    sleep_ms(200)

def waitForSw():                          # waits for a switch change
   while switch.value() == 0:
    pass

redLedOff()                               # turn all leds off to start
greenLedOff()
blueLedOff()
sleep_ms(500)                            # when uploaded all leds turn on (white) for a 200 or so ms.  Tried this to fix it.  Helped but did not work

while True:                               # main loop

  redLedOff()						
  greenLedOff()
  blueLedOn()					                    # turn blue led on
  deBounce()
  waitForRel()
  waitForSw()

  redLedOn()					                    # turn red led on
  blueLedOff()                 
  greenLedOff()
  deBounce()
  waitForRel() 
  waitForSw()

  redLedOff()
  greenLedOn()				                    # turn green led on
  blueLedOff()
  deBounce()
  waitForRel()
  waitForSw()
  
  redLedOff()					                    # turn turquoise on (blue+green)
  greenLedOn()
  blueLedOn()
  deBounce()
  waitForRel()
  waitForSw()

  redLedOn()					                    # turn purple on (red+blue)
  greenLedOff()
  blueLedOn()
  deBounce()
  waitForRel()
  waitForSw()

  redLedOn()					                    # turn orange on (red+green)
  greenLedOn()
  blueLedOff()
  deBounce()
  waitForRel()
  waitForSw()

  redLedOff()					                    # all off
  greenLedOff()
  blueLedOff()
  deBounce()
  waitForRel()
  waitForSw()



 
 
  
