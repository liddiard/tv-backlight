from machine import Pin, I2C
from time import sleep_ms

phase = 0
firstLoop = True
maxPhase = 7

led_r = Pin(20, Pin.OUT, Pin.PULL_UP)     # tried pull-up for red, since it is always "on" slightly.  Did not help
led_g = Pin(19, Pin.OUT)
led_b = Pin(18, Pin.OUT)
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

  
def debounce():
    print("debouncing:")
    debounced = False
    count = 0
    limit = 50
    #sleep_ms(25)
    while debounced == False:
        if switch.value() == 1:
            count += 1
        else:
            count = 0
        if count >= limit:
            debounced = True
            
def waitForRelease():
    while switch.value() == 1:
        sleep_ms(300)
        
def waitForSwitch():
    while switch.value() == 0:
        pass
        
def updateDisplay():
    global phase
    phase += 1
    if phase > maxPhase:
        phase = 1
    if phase == 1:
        redLedOn()
        greenLedOff()
        blueLedOff()
    elif phase == 2:
        redLedOff()
        greenLedOn()
        blueLedOff()        
    elif phase == 3:
        redLedOff()
        greenLedOff()
        blueLedOn()
    elif phase == 4:
        redLedOff()
        greenLedOn()
        blueLedOn()
    elif phase == 5:
        redLedOn()
        greenLedOff()
        blueLedOn()
    elif phase == 6:
        redLedOn()
        greenLedOn()
        blueLedOff()        
    elif phase == 7:
        redLedOff()
        greenLedOff()
        blueLedOff()
    else:
        redLedOff()
        greenLedOff()
        blueLedOff()

        
while True:
    updateDisplay()
    if not firstLoop:
        debounce()
        waitForRelease()
    waitForSwitch()
    firstLoop = False


        