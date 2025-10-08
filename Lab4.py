import time
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pinArray = [17, 27, 22, 23, 24, 25, 16, 20, 21, 26]
pwmArray = []
catchPin = 4

for i in range(10):
	GPIO.setup(pinArray[i],GPIO.OUT)

GPIO.setup(catchPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def myCallback(pin)

	phase *= -1

GPIO.add_event_detect(catchPin, GPIO.RISING, callback = myCallback, bouncetime = 100)

f = 0.2
phase = math.pi/11
f_base = 500

for i in range(10):
	pwmTemp = GPIO.PWM(pinArray[i],f_base)
	pwmArray.append(pwmTemp)

try:
	t = time.time()
	for i in range(10):
		pwmArray[i].start(100 * ((sin(2 * math.pi * f * t - phase * i)) ** 2))
except KeyboardInterrupt:
	GPIO.cleanup()
	for i in range(10):
		pwmArray[i].stop()