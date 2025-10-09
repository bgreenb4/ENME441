import random as random
import time
import RPi.GPIO as GPIO
from shifter import ShifterClass

serialPin, latchPin, clockPin = 23, 24, 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial = 0)
GPIO.setup(clockPin, GPIO.OUT, initial = 0)

shift = ShifterClass(serialPin, clockPin, latchPin)

pattern = [1,2,4,8,16,32,64,128]
location = 0

def walk():
	global pattern
	global location
	
	rand = random.choice([-1,1])
	location = location + rand
	if location < 0:
		location = 0
	if location > 7:
		location = 7
		
	return location

try:
	while 1:
		walk()
		print(pattern[location])
		shift.shiftByte(pattern[location])
		time.sleep(0.05)
except KeyboardInterrupt:
	print('\nExiting')
	GPIO.cleanup()

