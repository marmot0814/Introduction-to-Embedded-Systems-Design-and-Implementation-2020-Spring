import schedule
import time
import picamera
from datetime import datetime
import subprocess

def job():
    print ("I'm working...")


camera = picamera.PiCamera()
time.sleep(2)

subprocess.run(['rm', '-rf', 'jpg', 'jpg.zip'])
subprocess.run(['mkdir', 'jpg'])

num = 3
while num >= 0:
    camera.capture('jpg/' + '|'.join(datetime.now().__str__().split(' ')) + '.jpg')
    num -= 1
    time.sleep(1)
    print ("take a picture")

subprocess.run(['zip', '-r', 'jpg.zip', 'jpg'])
subprocess.run(['scp', 'jpg.zip', 'marmot0814@192.168.43.253:~/Downloads'])
