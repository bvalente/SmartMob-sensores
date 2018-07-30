import RPi.GPIO as GPIO
import time

PIN = 17 #GPIO
TIME = 0.2 #duration of beep

def start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.OUT)
    
def beep():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(TIME)
    
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(TIME/2.0)
    

if __name__ == '__main__':
	start()
	beep()
	GPIO.cleanup()