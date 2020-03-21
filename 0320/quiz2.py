import sys
sys.path.append('..')

import RPi.GPIO as GPIO
from utils.led import LED
from utils.dht11 import DHT11
from utils.hcsr04 import HCSR04
from utils.func import speed_of_sound, now
import time
import datetime

def main():

    # create LED component
    led = LED(7)

    # create DHT-11 component
    dht11 = DHT11(11)

    # create HC-SR04 component
    hcsr04 = HCSR04(13, 15)

    while True:

        # read current temperature and humidity
        t, h = dht11.read()

        # read distance from ultrasonic device
        d = hcsr04.read(speed_of_sound(t))

        # Safe mode
        if d >= 100:
            continue
        
        # be careful or dangerous
        led.on()
        time.sleep(0.1 if d < 30 else 0.5)
        led.off()
        time.sleep(0.1 if d < 30 else 0.5)

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
