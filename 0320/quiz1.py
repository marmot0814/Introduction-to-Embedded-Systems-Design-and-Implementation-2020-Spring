import sys
sys.path.append('..')

import RPi.GPIO as GPIO
from utils.led import LED
from utils.dht11 import DHT11
import datetime
import time

def main():
    dht11 = DHT11(11)
    led = LED(7)
    while True:
        t, h = dht11.read()
        if t >= 26:
            led.on()
        else:
            led.off()
        time.sleep(0.5)

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
