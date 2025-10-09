import time
import RPi.GPIO as GPIO
from shifter import ShifterClass
from Bug import BugClass

serialPin, latchPin, clockPin = 23, 24, 25
onCatch, wrapCatch, speedCatch = 16, 20, 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial = 0)
GPIO.setup(clockPin, GPIO.OUT, initial = 0)

GPIO.setup(onCatch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(wrapCatch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(speedCatch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def onCallback(pin):
	global bugout
	bugout.stop()

GPIO.add_event_detect(onCatch, GPIO.RISING, callback = onCallback, bouncetime = 100)

shift = ShifterClass(serialPin, clockPin, latchPin)
bugout = BugClass(shift)