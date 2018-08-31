#!/usr/bin/env python3

#SmartMob
#Tap Module

import RPi.GPIO as GPIO
from time import sleep

red_pin = 16
green_pin = 18
blue_pin = 22
freq = 100

RED = None
GREEN = None
BLUE = None

def setup(r, g, b, mode=1): # mode=1 -> GPIO.BOARD; mode=2 -> GPIO.BCM
    if (mode == 1):
        GPIO.setmode(GPIO.BOARD)
    elif (mode == 2):
        GPIO.setmode(GPIO.BCM)
    else:
        print("Invalid GPIO mode")
        return

    global red_pin
    global green_pin
    global blue_pin
    red_pin = r
    green_pin = g
    blue_pin = b

    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(blue_pin, GPIO.OUT)

    global RED
    global GREEN
    global BLUE
    RED = GPIO.PWM(red_pin, freq)
    GREEN = GPIO.PWM(green_pin, freq)
    BLUE = GPIO.PWM(blue_pin, freq)

    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)

def LED_color(r, g, b, pause):
    global RED
    global GREEN
    global BLUE
    
    if (RED is not None):
        RED.ChangeDutyCycle(r)
    else:
        print("Error")
    if (GREEN is not None):    
        GREEN.ChangeDutyCycle(g)
    else:
        print("Error")
    if (BLUE is not None):
        BLUE.ChangeDutyCycle(b)
    else:
        print("Error")

    sleep(pause)

    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)

if __name__ == '__main__': # Example of possible usage
    setup(16,18,15)
    try:
        while True:
            for x in range(0,2):
                for y in range(0,2):
                    for z in range(0,2):
                        print (x,y,z)
                        for i in range(0,101):
                            LED_color((x*i),(y*i),(z*i),.02)
    except KeyboardInterrupt:
        GPIO.cleanup()
