import time
import RPi.GPIO as GPIO
from shifter import ShifterClass
from Bug import BugClass

serialPin, latchPin, clockPin = 23, 24, 25
onCatch, wrapCatch, speedCatch = 16, 20, 21
onState, wrapState, speedState = False, False, False

GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial = 0)
GPIO.setup(clockPin, GPIO.OUT, initial = 0)

GPIO.setup(onCatch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(wrapCatch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(speedCatch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def onCallback(pin):
	global onState
	onState = True

def wrapCallback(pin):
	global wrapState
	wrapState = True

def speedUpCallback(pin):
	global speedState
	speedState = True

def run():
	if onState == True:
		bugout.start()
	else:
		bugout.stop()
	if wrapState == True:
		bugout = BugClass(shift, True)
	else:
		bugout = BugClass(shift)
	if speedState == True:
		bugout = BugClass(shift, 0.03)
	else:
		bugout = BugClass(shift)

GPIO.add_event_detect(onCatch, GPIO.RISING, callback = onCallback, bouncetime = 100)
GPIO.add_event_detect(wrapCatch, GPIO.RISING, callback = wrapCallback, bouncetime = 100)
GPIO.add_event_detect(speedCatch, GPIO.RISING, callback = speedUpCallback, bouncetime = 100)

shift = ShifterClass(serialPin, clockPin, latchPin)
bugout = BugClass(shift)

try:
	while 1:
		run()
except KeyboardInterrupt:
	print("Exiting")
	GPIO.cleanup()