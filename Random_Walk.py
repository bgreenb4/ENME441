from Shifter import Shifter
import time
import random
import RPi.GPIO as GPIO

Shifter = Shifter(23, 24, 25)
pattern = 0b00000000

rand = random(1,2)
pixel = 0

if pixel == 0:
	pixel = pixel + 1
else if pixel == 7:
	pixel = pixel - 1
else:
	if rand == 1:
		pixel = pixel - 1
	if rand == 2:
		pixel = pixel + 1

if pixel == 0:
	pattern = 0b00000001
if pixel == 0:
	pattern = 0b00000010
if pixel == 0:
	pattern = 0b00000100
if pixel == 0:
	pattern = 0b00001000
if pixel == 0:
	pattern = 0b00010000
if pixel == 0:
	pattern = 0b00100000
if pixel == 0:
	pattern = 0b01000000
if pixel == 0:
	pattern = 0b10000000

try:
	while 1:
		shiftByte(pattern)
		time.sleep(0.05)
except:
	GPIO.cleanup()