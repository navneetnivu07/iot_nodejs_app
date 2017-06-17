# Project : IoT Home Automation
# Author: Navaneeth M
# Target Board : RaspberryPi 3 Model B

import RPi.GPIO as GPIO
import json
import time
import threading
import requests

# Button Configurations
GPIO.setmode(GPIO.BOARD)

s1 = 07  
s2 = 11 


switch2room = {
	s1: '{"topic":"control/n1","pin":2}',
	s2: '{"topic":"control/n1","pin":4}',

}	

GPIO.setwarnings(False) # because I'm using the pins for other things too!
GPIO.setup([s1,s2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

################################### Button Configurations End


#Interrupt Handler Functions
i = 0
def handle(pin):
	global i
	print i
	print "pin : " + str(pin)
	node_data = json.loads(switch2room[pin])
	pub_msg = {"action":GPIO.input(pin),"pin":node_data['pin']}
	#print "action : " + str(GPIO.input(pin))	
	print("json publish ::: topic : " + node_data['topic'] + ", message : " + json.dumps(pub_msg))
	#print "action : " + str(GPIO.input(pin))	
	print " "
	i+= 1

GPIO.add_event_detect(s1, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s2, GPIO.BOTH, handle, bouncetime=50)


#######################################Interrupt Handler Functions End

while True:
	time.sleep(1e6)
