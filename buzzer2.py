import RPi.GPIO as GPIO
import time

pin = 3
TIME = 2
matrix =[0.1, 131, 147, 165, 175, 196, 211, 248]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

'''
GPIO.output(pin, GPIO.HIGH)
time.sleep(1)
GPIO.output(pin, GPIO.LOW)
'''

p = GPIO.PWM(pin, 1)
p.start(50)
'''
p.ChangeFrequency(200)
time.sleep(TIME)
p.ChangeFrequency(50)
time.sleep(TIME)
'''
for f in matrix:
    print(f)
    p.ChangeFrequency(f)
    time.sleep(TIME)
    

p.stop()


GPIO.cleanup()