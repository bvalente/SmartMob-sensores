# from https://www.14core.com/wiring-the-passive-active-buzzer-with-raspberry-pi/
#Passive buzzer example
import sys, json
RASPBERRY = False
if RASPBERRY == True:
    import RPi.GPIO as GPIO   #import the GPIO library
from time import sleep   #import the time library



SLEEP_TIME = 0.5



def read_sensor_info(sensor_type):
    with open('sensor_config.txt') as json_data:
        sensor = json.load(json_data)
        print('sensor_config: ', sensor)
        json_data.close()
    return sensor[sensor_type]

def gpio_init():
    if RASPBERRY == True:
        GPIO.setmode(GPIO.BOARD)

def start_vib_sensor(sensor):
    if RASPBERRY == True:
        GPIO.setup(sensor['pin'],GPIO.IN)
    return sensor

def detect_vibration(sensor):
    vibrationEvent = False
    while not vibrationEvent:
        if GPIO.input(sensor['pin']):
            vibrationEvent = True:
        sleep(SLEEP_TIME) 

def stop_gpio():
    if RASPBERRY == True:
        GPIO.cleanup()


my_sensor = {}
my_sensor = read_sensor_info('vibration')
start_gpio()

my_sensor = start_vib_sensor(my_sensor)
print (my_sensor)

print ('start test mode')

detect_vibration(my_sensor)

print ('Stop test mode\n')

stop_gpio()
