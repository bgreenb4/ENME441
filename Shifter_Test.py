from Shifter import Shifter
import time
import random
import RPi.GPIO as GPIO

serialPin, latchPin, clockPin = 23, 24, 25  
GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)
GPIO.setup(clockPin, GPIO.OUT, initial=0)

shifter = Shifter(serialPin, latchPin, clockPin)

try:
	while 1:
		for i in range(2**8):
			shifter.shiftByte(i)
			print(i)
			time.sleep(0.5)
		
except KeyboardInterrupt:
	GPIO.cleanup()


