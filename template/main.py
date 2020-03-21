import sys
sys.path.append('..')

import RPi.GPIO as GPIO

def main():
    pass

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
