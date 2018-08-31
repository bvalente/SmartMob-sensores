import RPi.GPIO as GPIO
import time

#semaforo

greenPIN = 16
redPIN = 18
bluePIN = 15
TIME = 2


def start():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(greenPIN, GPIO.OUT)
    GPIO.output(greenPIN, GPIO.LOW)

    GPIO.setup(redPIN, GPIO.OUT)
    GPIO.output(redPIN, GPIO.LOW)

    GPIO.setup(bluePIN, GPIO.OUT)
    GPIO.output(bluePIN, GPIO.LOW)

def stop():
    greenOFF()
    redOFF()
    blueOFF()

def greenON():
    GPIO.output(greenPIN, GPIO.HIGH)

def greenOFF():
    GPIO.output(greenPIN, GPIO.LOW)

def redON():
    GPIO.output(redPIN, GPIO.HIGH)

def redOFF():
    GPIO.output(redPIN, GPIO.LOW)

def blueON():
    GPIO.output(bluePIN, GPIO.HIGH)

def blueOFF():
    GPIO.output(bluePIN, GPIO.LOW)


if __name__ == '__main__': # Example of possible usage
    start()
    try:
        while True:
            redON()
            sleep(1)
            redOFF()

            greenON()
            sleep(1)
            greenOFF()

            blueON()
            sleep(1)
            blueOFF()

            #end cycle
    except KeyboardInterrupt:
        stop()
