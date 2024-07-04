from machine import Pin,PWM
import utime
import random
Led_R = PWM(Pin(15))
Led_G = PWM(Pin(16))
Led_B = PWM(Pin(17))
# Define the frequency
Led_R.freq(500)   # was 2000
Led_G.freq(500)   # was 2000
Led_B.freq(500)   # was 2000
if __name__ == "__main__":
    while True:
        # range of random numbers
        R=random.randint(0,65535)      
        G=random.randint(0,65535)
        B=random.randint(0,65535)
        print(R,G,B)   
        Led_R.duty_u16(R)
        Led_G.duty_u16(G)
        Led_B.duty_u16(B) 
        utime.sleep_ms(300)  # was 100