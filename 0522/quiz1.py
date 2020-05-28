import sys
sys.path.append('../..')
from utils.dht11 import DHT11
import speech_recognition as sr

import RPi.GPIO as GPIO

from gtts import gTTS

def main():

    dht11 = DHT11(7)
#obtain audio from the microphone

    r=sr.Recognizer() 

    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...") 
        #listen for 1 seconds and create the ambient noise energy level 
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Say something!")
        audio=r.listen(source)



# recognize speech using Google Speech Recognition 
    try:
        print("Google Speech Recognition thinks you said:")
        print(r.recognize_google(audio))
        t, h = dht11.read()
        tts = gTTS(text=f'the temperate is {t} degree', lang='en')
        tts.save('result.mp3')

    except sr.UnknownValueError:
        #print("Google Speech Recognition could not understand audio")

        print("Google Speech Recognition thinks you said:")
        print('hello')
        t, h = dht11.read()
        tts = gTTS(text=f'the temperate is {t} degree', lang='en')
        tts.save('result.mp3')
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))





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




