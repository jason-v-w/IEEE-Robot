#!/usr/bin/python

import sys
from Adafruit_PWM_Servo_Driver import PWM
import time

print len(sys.argv)
print str(sys.argv)

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def setServoAngle(channel, angle, freq):
  period = 1.0/freq
  pulseLength = 20                        #set to 20ms for 50Hz
  setPoint = 4096/(pulseLength/(0.5 + angle/180.0*1.88)) #servo runs between 0.5ms (0deg) and 2.5ms (180deg)
  pwm.setPWM(channel, 0, int(setPoint))
  

pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
##pwm.setPWM(0, 0, servoMin)
##time.sleep(1)
##pwm.setPWM(0, 0, servoMax)
##time.sleep(1)
##pwm.setPWM(1, 0, servoMin)
##time.sleep(1)
##pwm.setPWM(1, 0, servoMax)
##time.sleep(1)
##  pwm.setPWM(0, 0, 512)
##  time.sleep(1)
##  pwm.setPWM(0, 0, 102)
##  time.sleep(1)
##  pwm.setPWM(0, 0, 307)
##  time.sleep(1)
  setServoAngle(0,10,50)
  setServoAngle(1,10,50)
  time.sleep(3)
  setServoAngle(0,45,50)
  setServoAngle(1,45,50)
  time.sleep(1)
  setServoAngle(0,90,50)
  setServoAngle(1,90,50)
  time.sleep(1)
  setServoAngle(0,135,50)
  setServoAngle(1,135,50)
  time.sleep(1)
  setServoAngle(0,180,50)
  setServoAngle(1,180,50)
  time.sleep(3)
  setServoAngle(0,135,50)
  setServoAngle(1,135,50)
  time.sleep(1)
  setServoAngle(0,90,50)
  setServoAngle(1,90,50)
  time.sleep(1)
  setServoAngle(0,45,50)
  setServoAngle(1,45,50)
  time.sleep(1)
##pwm.setPWM(0, 0, 900)
##time.sleep(1)
##setServoPulse(0,1)
##time.sleep(1)
##setServoPulse(0,2)



