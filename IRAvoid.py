#!/usr/bin/env python3

#SmartMob
#Infrared Avoidance Sensor Module without Enable

import RPi.GPIO as GPIO

ObstaclePin = 16 # change to the pin you want to use

def setup():
    GPIO.setmode(GPIO.BOARD) # set GPIO by pin numbers
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def detect(): # returns 1 if obstacle is detected
    try:
        edge = GPIO.wait_for_edge(ObstaclePin, GPIO.FALLING) # you can add a time limit as a
        if edge is None:                                     # third argument in ms
            print("Time out ocurred")
            return 0
        else:
            print("Obstacle found")
            return 1
        
    except KeyboardInterrupt:
        terminate()
        return 0

def terminate():
    GPIO.cleanup() # releases resources
