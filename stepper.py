import sys
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


StepPins = [17,22,23,24]


for pin in StepPins:
  print ("Setup pins")
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

StepCount = len(Seq)
StepDir = 1

if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 1/float(1000)

StepCounter = 0

while True:
        direction = input("CCW or CW")
        numSteps = input("How many steps")
        if (direction.lower() == "CW"):
                StepDir = 1
        else:
                StepDir = -1
for turns in range(0, numSteps):
        print (StepCounter)
        print (Seq[StepCounter])
        for pin in range (0,4):
                xpin = StepPins[pin]
                if Seq[StepCounter][pin]!=0:
                        print ("Enable GPIO %i" %(xpin)
                        GPIO.output(xpin, True)
                else:
                        GPIO.output(xpin, False)

        StepCounter += StepDir

        if (StepCounter>=StepCount):
                StepCounter = 0
        if (StepCounter<0):
                StepCounter = StepCount+StepDir


        time.sleep(WaitTime)
