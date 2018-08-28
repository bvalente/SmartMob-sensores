#!/usr/bin/env python3

#SmartMob
#Black or White surface
#returns 1 in presence of black surface
#returns 0 in presence of white surface

import RPi.GPIO as GPIO
from time import sleep

pin = 16

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)

def detect():
    return  GPIO.input(pin)

if __name__ == '__main__': # Program starts running here
    setup()

    while True:
        sleep(1)

        print ( detect() )
