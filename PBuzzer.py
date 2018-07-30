import RPi.GPIO as GPIO
import time

PIN = 3
TIME = 0.5
matrix =[131, 147, 165, 175, 196, 211, 248]

def start():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.OUT)
    
def test():
    p = GPIO.PWM(PIN, matrix[0])
    print(matrix[0])
    
    p.start(50) #50 is duty cycle
    
    for f in matrix[1:]:
        time.sleep(TIME)
        print(f)
        p.ChangeFrequency(f)
    time.sleep(TIME) #sound last value in matrix
    
    p.stop()
    
def beep():
    
    p = GPIO.PWM(PIN, 150)
    p.start(50) #50 is duty cycle
    
    #beep
    time.sleep(TIME)
    
    #silence
    p.ChangeDutyCycle(0)
    time.sleep(TIME)
    
    #beep
    p.ChangeDutyCycle(50)
    time.sleep(TIME)
    
    #end
    p.stop()
    
start()
#test()
beep()

GPIOO.cleanup()