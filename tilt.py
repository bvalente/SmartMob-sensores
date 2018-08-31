#!/usr/bin/env python3

#SmartMob
#Tap Module

import RPi.GPIO as GPIO
from time import sleep

pin = 16

def setup(pin, mode=1): # mode=1 -> GPIO.BOARD; mode=2 -> GPIO.BCM
    if (mode == 1):
        GPIO.setmode(GPIO.BOARD)
    elif (mode == 2):
        GPIO.setmode(GPIO.BCM)
    else:
        print("Invalid GPIO mode")
        return

    GPIO.setup(pin, GPIO.IN)


def terminate():
    GPIO.cleanup() # releases resources

if __name__ == '__main__': # Example of possible usage
    setup(16)
    while True:
        print(GPIO.input(pin))
        sleep(1)
