import RPi.GPIO as GPIO
import time

#semaforo

greenPIN = 3
redPIN = 5
TIME = 2


def start():
    time.sleep(TIME)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(greenPIN, GPIO.OUT)
    GPIO.output(greenPIN, GPIO.LOW)
    GPIO.setup(redPIN, GPIO.OUT)
    GPIO.output(redPIN, GPIO.LOW)
    time.sleep(TIME)
    
def green():
    GPIO.output(greenPIN, GPIO.HIGH)
    GPIO.output(redPIN, GPIO.LOW)
    
def red():
    GPIO.output(redPIN, GPIO.HIGH)
    GPIO.output(greenPIN, GPIO.LOW)
    
def yellow():
    GPIO.output(redPIN, GPIO.HIGH)
    GPIO.output(greenPIN, GPIO.HIGH)
    
def stop():
    GPIO.output(redPIN, GPIO.LOW)
    GPIO.output(greenPIN, GPIO.LOW)
    time.sleep(TIME)
    
    
start()
green()
time.sleep(TIME)
yellow()
time.sleep(TIME)
red()
time.sleep(TIME)
stop()
GPIO.cleanup()