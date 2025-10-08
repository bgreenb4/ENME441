from Shifter import Shifter
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Shifter = Shifter(23, 24, 25)
pattern = 0b00000001
pixel = 0

def walk():
	global pattern
	global pixel
	
	rand = random.choice([-1,1])
	pixel = pixel + rand
	if pixel < 0:
		pixel = 0
	if pixel > 7:
		pixel = 7
	
	if pixel == 0:
		pattern = 0b00000001
	if pixel == 1:
		pattern = 0b00000010
	if pixel == 2:
		pattern = 0b00000100
	if pixel == 3:
		pattern = 0b00001000
	if pixel == 4:
		pattern = 0b00010000
	if pixel == 5:
		pattern = 0b00100000
	if pixel == 6:
		pattern = 0b01000000
	if pixel == 7:
		pattern = 0b10000000
	
	pattern = 1 << pixel
	return pattern

try:
	while 1:
		#walk()
		#print(pixel)
		#print(format(pattern, '08b'))

		for i in range(2**8):
			Shifter.shiftByte(i)
			print(i)
			time.sleep(0.5)

except KeyboardInterrupt: # if user hits ctrl-C
	print('\nExiting')
	GPIO.cleanup()
