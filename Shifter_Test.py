from Shifter import Shifter
import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
Shifter = Shifter(23,24,25)

try:
	while 1:
		Shifter.shiftByte(0b00000000)
		time.sleep(0.5)
		Shifter.shiftByte(0b11111111)
except KeyboardInterrupt:
	GPIO.cleanup()