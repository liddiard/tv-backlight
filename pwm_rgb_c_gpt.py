
from machine import Pin, PWM
import time

# Define the RGB LED pins
red_pin = Pin(15, Pin.OUT)  # Replace with the actual pin number
green_pin = Pin(17, Pin.OUT)  # Replace with the actual pin number
blue_pin = Pin(16, Pin.OUT) # Replace with the actual pin number

# Create PWM objects for each color
red_pwm = PWM(red_pin, freq=1000)
green_pwm = PWM(green_pin, freq=1000)
blue_pwm = PWM(blue_pin, freq=1000)

# Given brightness value between 0 and 1, set PWM value between 0 = 100% on and 65536 = off
def set_brightness(pwm, brightness):   
    max_duty_cycle = 2**16
    duty = max_duty_cycle - (brightness * max_duty_cycle)
    print (duty, "in set brightnes")
    pwm.duty_u16(round(duty))

def set_color(red, green, blue):
    # Set the duty cycle for each color (0-1023)
    set_brightness(red_pwm, red)
    set_brightness(green_pwm, green)
    set_brightness(blue_pwm, blue) 
    

def loop_colors():     
    while True:
        print("in looop")
        # purple
        set_color(.5, 0, 1)
        time.sleep(2)

        # Green
        set_color(.5, 0, 0)
        time.sleep(2)

        # Blue
        set_color(0, 0, 1)
        time.sleep(2)

        # Yellow (Red + Green)
        set_color(1, 1, 0)
        time.sleep(2)

        # Magenta (Red + Blue)
        set_color(1, 0, 1)
        time.sleep(2)

        # Cyan (Green + Blue)
        set_color(0, 1, 1)
        time.sleep(2)

# Run the color loop
loop_colors()