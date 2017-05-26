import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

client = mqtt.Client()
client.connect("192.168.1.16", 1883, 60)
client.loop_start()

switch_1 = 11

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(switch_1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
previous_state = 2
j = 1

while True:
	
	i = GPIO.input(switch_1)
	if i==0:
		if previous_state != i:
			client.publish("control/n1", i)
			print "%d) %d "%(j,i)
			previous_state = i
			j+=1
	elif i==1:
		if previous_state != i:
			client.publish("control/n1", i)
			print "%d) %d "%(j,i)
			previous_state = i
			j+=1
		
