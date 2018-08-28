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
    
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def detect(): # returns 1 if obstacle is detected
    try:
        edge = GPIO.wait_for_edge(pin, GPIO.FALLING) # you can add a time limit as a
        if edge is None:                                     # third argument in ms
            print("Time out ocurred")
            return 0
        else:
            print("Tap")
            sleep(.3)
            return 1
        
    except KeyboardInterrupt:
        terminate()
        return 0

def terminate():
    GPIO.cleanup() # releases resources

if __name__ == '__main__': # Example of possible usage
    setup(16)
    while True:
        detect()
