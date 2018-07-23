# from https://www.14core.com/wiring-the-passive-active-buzzer-with-raspberry-pi/
#Passive buzzer example
import sys, json
RASPBERRY = False
if RASPBERRY == True:
    import RPi.GPIO as GPIO   #import the GPIO library
from time import sleep   #import the time library


freq_matrix = [[0, 131, 147, 165, 175, 196, 211, 248],
        [0, 262, 294, 330, 350, 393, 441, 495],
        [0, 525, 589, 661, 700, 786, 882, 990]]

DUTY_CYCLE = 50
MIN_TIME = 5


def read_sensor_info(sensor_type):
    with open('sensor_config.txt') as json_data:
        sensor = json.load(json_data)
        print('sensor_config: ', sensor)
        json_data.close()
    return sensor[sensor_type]

def start_gpio():
    if RASPBERRY == True:
        GPIO.setmode(GPIO.BOARD)

def start_passive_buzzer(sensor):
    if RASPBERRY == True:
        GPIO.setup(sensor['pin'],GPIO.OUT)
        GPIO.output(sensor['pin'],GPIO.LOW)
        sensor['pmw_control'] = GPIO.PWM(sensor['pin'],sensor['freq'])
        sensor['pmw_control'].start(DUTY_CYCLE)
    else:
        sensor['pmw_control']=33
    return sensor

def test_buzzer(sensor, test_freq):
    print (test_freq)
    for i in range(len(test_freq)):
        for j in range(len(test_freq[0])):
            set_buzzer(sensor, test_freq[i][j])

def set_buzzer (sensor, freq):
    print ('buzzer[pmw_control].ChangeFrequency: {}'.format(freq))
    sensor['freq']=freq
    if RASPBERRY == True:
        sensor['pmw_control'].ChangeFrequency(sensor['pin'],freq)
        sleep(MIN_TIME)
    return (sensor)

def stop_passive_buzzer(sensor):
    if RASPBERRY == True:
        sensor['pmw_control'].stop()
        GPIO.output(sensor['pin'],GPIO.HIGH)

def stop_gpio():
    if RASPBERRY == True:
        GPIO.cleanup()

my_sensor = {}
my_sensor = read_sensor_info('buzzer')
start_gpio()
my_sensor = start_passive_buzzer(my_sensor)
print (my_sensor)

print ('Start test mode')
print ('Global frequency test\n')
test_buzzer (my_sensor, freq_matrix)
print ('Selected frequency test\n')
freq = input ('Press a frequency to continue.')
print (freq)
my_sensor= set_buzzer (my_sensor, int(freq))
print (my_sensor)
print ('Stop test mode\n')

stop_passive_buzzer(my_sensor)
stop_gpio()
