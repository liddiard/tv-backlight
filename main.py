# inspiration from multiple sites, but started with https://www.youngwonks.com/blog/How-to-use-an-RGB-LED-with-the-Raspberry-Pi-Pico
# Needed to invert the outputs since it is an common anode LED
# the button pushes were unpredictible, so pretty much all re-written with Bill.  I suck :( 
# Many modes.  Bill figured out it will work if I totally remove the resistor (which the leaves no current limiting)
# July 15, 2024: uploaded to the pico, and put it in a box.  Seems to work, but will skip sometimes. No problem.

from machine import Pin
from time import sleep_ms

# constants
led_r = Pin(18, Pin.OUT, Pin.PULL_UP)     # 24K ohms worth of restiors to 3.3v VCC 
led_g = Pin(19, Pin.OUT)
led_b = Pin(20, Pin.OUT)
switch = Pin(27, Pin.IN, Pin.PULL_DOWN)

# r, g, b
colors = [
  (0, 0, 1), # blue
  (1, 0, 0), # red
  (0, 1, 0), # green
  (1, 1, 0), # yellow
  (1, 0, 1), # magenta
  (0, 1, 1), # cyan
]

# state variables
cur_color = 0 # index of current color

def set_color(color):
  """
  Sets the color of the RGB LED based on the input color tuple.

  Args:
      color (tuple): A tuple representing the RGB values to set. Each value should be in the range of 0 to 1.

  Returns:
      None
  """
  led_r.value(color[0])
  led_g.value(color[1])
  led_b.value(color[2])

def set_next_color():
  """
  Increment the current color index and set the next color based on the updated index.
  """
  cur_color = (cur_color + 1) % len(colors)
  set_color(colors[cur_color])

def debounce():
  # print("debouncing")
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
        # print("leaving debounce")

set_color(1, 1, 1) # turn all LEDs on to start
sleep_ms(500)
set_color(colors[0]) # set to the first color

while True:
  if switch.value() == 1: # switch is pressed
    set_next_color()
    # wait for the switch to be released
    debounce()