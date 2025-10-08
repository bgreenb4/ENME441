import RPi.GPIO as GPIO
import time

class Shifter:
  def __init__(self, serialPin, clockPin, latchPin):
    self.serialPin = serialPin
    self.clockPin = clockPin
    self.latchPin = latchPin 
  
  def __ping(self, p):
    GPIO.output(p,1)
    time.sleep(0)
    GPIO.output(p,0)
  
  def shiftByte(self, b):
    for i in range(8):
      GPIO.output(self.serialPin, (b>>i) & 1)
      self.__ping(self.clockPin)
    self.__ping(self.latchPin)
