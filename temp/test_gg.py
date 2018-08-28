#!/usr/bin/env python3

#SmartMob
#Rotary encoder Module

import RPi.GPIO as GPIO
from time import sleep

pin = 15

posCount = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)

def start():
    GPIO.add_event_detect(pin, GPIO.RISING, callback=button, bouncetime=2)

def button(pin):
    print("button")

if __name__ == '__main__': # Program starts running here
    setup()
    start()
    while True:
        sleep(1)
