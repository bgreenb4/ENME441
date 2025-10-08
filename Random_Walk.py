from Shifter import Shifter
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Shifter = Shifter(23, 24, 25)
#pattern = 0b00000001
pattern = [1,2,4,8,16,32,64,128]
location = 0

def walk():
	global pattern
	global location
	
	rand = random.choice([-1,1])
	pixel = location + rand
	if location < 0:
		location = 0
	if location > 7:
		location = 7
		
	return pattern[location]

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

