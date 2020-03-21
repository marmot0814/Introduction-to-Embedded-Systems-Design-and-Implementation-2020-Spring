import RPi.GPIO as GPIO
from .func import log
import time

class HCSR04:

    def __init__(self, trigger_pin, echo_pin):
        self.__trigger_pin = trigger_pin
        self.__echo_pin = echo_pin

    def read(self, v = 343):
        GPIO.setup(self.__trigger_pin, GPIO.OUT)
        GPIO.output(self.__trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.__trigger_pin, GPIO.LOW)
        pulse_start = time.time()
        GPIO.setup(self.__echo_pin, GPIO.IN)
        while GPIO.input(self.__echo_pin) == GPIO.LOW:
            pulse_start = time.time()
        while GPIO.input(self.__echo_pin) == GPIO.HIGH:
            pulse_end = time.time()
        t = pulse_end - pulse_start
        d = t * v * 50
        print ("%s: 距離: %.02fcm" % (log("hcsr04"), d))
        return d
