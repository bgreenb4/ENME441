from Shifter import Shifter
import time
import random
import RPi.GPIO as GPIO

serialPin, latchPin, clockPin = 23, 24, 25  
GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)
GPIO.setup(clockPin, GPIO.OUT, initial=0)
'''
serialPin, latchPin, clockPin = 23, 24, 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)  # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0) 
def ping(p):
	GPIO.output(p,1)
	time.sleep(0)
	GPIO.output(p,0)
  
def shiftByte(b):
	for i in range(8):
		GPIO.output(serialPin, b & (1<<i))
		ping(clockPin)
	ping(latchPin)
    
try:
	while 1:
		for i in range(2**8):
			shiftByte(i)
			print(i)
			time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
'''

shifter = Shifter(serialPin, latchPin, clockPin)

try:
	while 1:
		for i in range(2**8):
			shifter.shiftByte(i)
			print(i)
			time.sleep(0.5)
		
except KeyboardInterrupt:
	GPIO.cleanup()

