import time
import RPi.GPIO as GPIO
from shifter import ShifterClass
from Bug import BugClass

serialPin, latchPin, clockPin = 23, 24, 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial = 0)
GPIO.setup(clockPin, GPIO.OUT, initial = 0)

shift = ShifterClass(serialPin, clockPin, latchPin)

bugout = BugClass(shift)



try:
    while True:
        bugout.start()
except:
    bugout.stop()
    GPIO.cleanup()
