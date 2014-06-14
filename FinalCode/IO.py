#!/bin/python


import RPi.GPIO as GPIO


lednumb=18
PIRnumb=26

def SetupGPIOPins():

	global PIRnumb
	global lednumb

	try:
		import RPi.GPIO as GPIO
	except RuntimeError:
        	print("error need run root")


	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(PIRnumb,GPIO.IN)
	GPIO.setup(lednumb,GPIO.OUT)
#	GPIO.setup(lednumb,GPIO.OUT,initial=GPIO.LOW)


def LEDON(): 

	global lednumb
	
	GPIO.output(lednumb,GPIO.HIGH)

def LEDOFF():

	global lednumb

	GPIO.output(lednumb,GPIO.LOW)



def Cleanup():

	GPIO.cleanup()







