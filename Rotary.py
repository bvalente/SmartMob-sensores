#!/usr/bin/env python3

#SmartMob
#Rotary encoder Module

import RPi.GPIO as GPIO
import signal
import sys
from time import sleep

posCount = 0
pinA = 16
pinB = 18

def terminate(signal, frame):
    print("Exiting")
    GPIO.cleanup() # releases resources
    sys.exit(0)

signal.signal(signal.SIGINT, terminate)

def setup(A, B, mode=1): # mode=1 -> GPIO.BOARD; mode=2 -> GPIO.BCM
    if (mode == 1):
        GPIO.setmode(GPIO.BOARD)
    elif (mode == 2):
        GPIO.setmode(GPIO.BCM)
    else:
        print("Invalid GPIO mode")
        return

    pinA = A
    pinB = B
    
    GPIO.setup(pinA, GPIO.IN)
    GPIO.setup(pinB, GPIO.IN)

def detect():
    GPIO.add_event_detect(pinA, GPIO.RISING, callback=rotationDecode, bouncetime=2)

def rotationDecode(pinA):
    global posCount
    c = posCount
    valA = GPIO.input(pinA)
    if valA == 0:
        return
    
    if (GPIO.input(pinB) != valA):
        posCount+=1
        CW = False

    else:
        CW = True
        posCount-=1

    #if CW:
    #    print("Rotated clockwise")
    #else:
    #    print("Rotated counter clockwise")

    #print(posCount)
    return CW

def terminate():
    print("Exiting")
    GPIO.cleanup() # releases resources

if __name__ == '__main__': # Program starts running here
    setup(16, 18)
    detect()
    #while True:
    #    sleep(1)
