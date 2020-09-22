from picamera import PiCamera
from os import path
from gpiozero import LED, Button
from time import sleep

led = LED(17)
doPowerOffButton = Button(4, pull_up=False)

for i in range(10):
    led.on()
    sleep(.05)
    led.off()
    sleep(.05)


doPowerOff = doPowerOffButton.is_pressed


def updateCount(newCount):
    with open('count.txt', 'w')as fh:
         fh.write(newCount)
         

if(not path.exists('count.txt')):
    updateCount('0')

camera = PiCamera()

with open('count.txt', 'r') as fh:
    photoId = fh.read()

    camera.capture('%s.jpg' % photoId)
    
    updateCount(str(int(photoId)+1))
    

if doPowerOff:
    import subprocess
    subprocess.Popen(['shutdown', '-h', 'now'])