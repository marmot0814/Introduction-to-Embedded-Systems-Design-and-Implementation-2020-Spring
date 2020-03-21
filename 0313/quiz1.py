import sys
sys.path.append('..')

import RPi.GPIO as GPIO
from utils.led import LED
import time

def main():
    led = LED(7)
    while True:
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)

def GPIO_init():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)

try:
    GPIO_init()
    main()

except KeyboardInterrupt:
    print ("exit")

finally:  
    GPIO.cleanup()
