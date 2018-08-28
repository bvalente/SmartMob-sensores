#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

LightInPin = 18 #Set GPIO Pin 11
counter = 0

def setup():
    GPIO.setmode(GPIO.BOARD) # Set GPIO as PIN Numbers
    GPIO.setup(LightInPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pull up to high level(3.3V)
    GPIO.add_event_detect(LightInPin, GPIO.RISING, callback=detect, bouncetime=200)


def detect(chn):
    global counter
    print ("Light has been interrupted")
    print ("counter: ",counter)
    counter+=1

def loop():
    while True:
        sleep(1)

def destroy():
    GPIO.cleanup() # Release resource

if __name__ == '__main__': # Set the Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When pressed 'Ctrl+C' child program destroy() will be executed.
        destroy()
