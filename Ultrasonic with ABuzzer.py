
import RPi.GPIO as GPIO
import time
import Ultrasonic as sonic
import ABuzzer as buzz

#main
buzz.PIN = 22 #mode BOARD
#buzz.TIME = 0.5

sonic.start()
buzz.start()

try:
	while True:
		dist = sonic.distance()
		print ("Distance = %.1f cm" % dist)
		if(dist < 20):
			buzz.beep()
		if(dist < 10):
			buzz.beep() #will have 2 beeps
		time.sleep(1)

	# Reset by pressing CTRL + C
except KeyboardInterrupt:
	print("Measurement stopped by User")
	GPIO.cleanup()

