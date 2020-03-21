import RPi.GPIO as GPIO

class LED:

    def __init__(self, pin):
        self.__pin = pin

    def on(self):
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin, GPIO.HIGH)

    def off(self):
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin, GPIO.LOW)
