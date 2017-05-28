# Project : IoT Home Automation
# Author: Navaneeth M
# Target Board : RaspberryPi 3 Model B

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
import time
import threading
import requests

# Button Configurations
GPIO.setmode(GPIO.BOARD)

s1 = 07 # Green IO
s2 = 11 # Green IO
s3 = 12 # Green IO
s4 = 13 # Green IO
s5 = 15 # Green IO
s6 = 16 # Green IO
s7 = 18 # Green IO
s8 = 19 # Pink IO
s9 = 21 # Pink IO
s10 = 22 # Green IO
s11 = 13 # Pink IO
s12 = 24 # Pink IO
s13 = 26 # Pink IO
s14 = 29 # Pure IO
s15 = 31 # Pure IO
s16 = 32 # Pure IO
s17 = 33 # Pure IO
s18 = 35 # Pure IO
s19 = 36 # Pure IO
s20 = 37 # Pure IO
s21 = 38 # Pure IO
s22 = 40 # Pure IO

switch2room = {
	s1: '{"topic":"control/n1","pin":2}',
	s2: '{"topic":"control/n1","pin":4}',
	
	s3: '{"topic":"control/n2","pin":2}',
	s4: '{"topic":"control/n2","pin":4}',
	s5: '{"topic":"control/n2","pin":5}',
	
	s6: '{"topic":"control/n3","pin":2}',
	s7: '{"topic":"control/n3","pin":4}',
	
	s8: '{"topic":"control/n4","pin":2}',
	s9: '{"topic":"control/n4","pin":4}',
	s10: '{"topic":"control/n4","pin":5}',
	
	s11: '{"topic":"control/n5","pin":2}',
	s12: '{"topic":"control/n5","pin":4}',
	
	s13: '{"topic":"control/n6","pin":2}',
	s14: '{"topic":"control/n6","pin":4}',
	s15: '{"topic":"control/n6","pin":5}',
	
	s16: '{"topic":"control/n7","pin":2}',
	s17: '{"topic":"control/n7","pin":4}',
	s18: '{"topic":"control/n7","pin":5}',
	
	s19: '{"topic":"control/n8","pin":2}',
	s20: '{"topic":"control/n8","pin":4}',
}	

GPIO.setwarnings(False) # because I'm using the pins for other things too!
GPIO.setup([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

################################### Button Configurations End

#MQTT Configurations

url = 'http://livemonitoring.info/node/ins.php'
headers = {'content-type': 'application/json'}

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("devices/status/#")

def on_message(client, userdata, msg):
    #print("Response : " + msg.topic+" "+str(msg.payload))
    response = requests.post(url, data=json.dumps(msg.payload), headers=headers)
    print response

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('ant', 'antWARE#07')
client.connect("192.168.1.42", 8883, 60)
client.loop_start()

##################################### MQTT Configurations End

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
	client.publish(node_data['topic'], json.dumps(pub_msg), 1)
	print " "
	i+= 1

GPIO.add_event_detect(s1, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s2, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s3, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s4, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s5, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s6, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s7, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s8, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s9, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s10, GPIO.BOTH, handle, bouncetime=50)
#GPIO.add_event_detect(s11, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s12, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s13, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s14, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s15, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s16, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s17, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s18, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s19, GPIO.BOTH, handle, bouncetime=50)
GPIO.add_event_detect(s20, GPIO.BOTH, handle, bouncetime=50)

#######################################Interrupt Handler Functions End

while True:
	time.sleep(1e6)

