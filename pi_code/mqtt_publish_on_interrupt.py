#!/usr/bin/python

# interrupt-based GPIO example using LEDs and pushbuttons
import paho.mqtt.client as mqtt
import json
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)

BTN_G = 11 # G17
BTN_R = 12 # G18
BTN_Y = 13 # G27
BTN_B = 15 # G22

LED_G = 29 # G5
LED_R = 31 # G6
LED_Y = 32 # G12
LED_B = 33 # G13

btn2led = {
	BTN_G: LED_G,
	BTN_R: LED_R,
	BTN_Y: LED_Y,
	BTN_B: LED_B,
}

switch2room = {
	BTN_G: '{"topic":"control/n1","pin":2}',
	BTN_R: '{"topic":"control/n1","pin":4}',
	BTN_Y: '{"topic":"control/n1","pin":5}'
}	

GPIO.setwarnings(False) # because I'm using the pins for other things too!
GPIO.setup([BTN_G, BTN_R, BTN_Y, BTN_B], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([LED_G, LED_R, LED_Y, LED_B], GPIO.OUT, initial=GPIO.HIGH)

# can't add separate callbacks for both rising and falling
#GPIO.add_event_detect(BTN_B, GPIO.RISING, lambda pin: GPIO.output(LED_B, False))
#GPIO.add_event_detect(BTN_B, GPIO.FALLING, lambda pin: GPIO.output(LED_B, True))

client = mqtt.Client()

client.username_pw_set('ant', 'antWARE#5747')
client.connect("192.168.1.16", 1883, 60)
client.loop_start()

def handle(pin):
	# light corresponding LED when pushbutton of same color is pressed
	print pin
	print GPIO.input(pin)	
	node_data = json.loads(switch2room[pin])
	print node_data['topic']
	print node_data['pin']
	pub_msg = {"action":GPIO.input(pin),"pin":node_data['pin']}
	print(json.dumps(pub_msg))
	client.publish(node_data['topic'], json.dumps(pub_msg), 1)

GPIO.add_event_detect(BTN_G, GPIO.BOTH, handle)
GPIO.add_event_detect(BTN_R, GPIO.BOTH, handle)
GPIO.add_event_detect(BTN_Y, GPIO.BOTH, handle)
GPIO.add_event_detect(BTN_B, GPIO.BOTH, handle)

# TODO: pause?
while True:
	time.sleep(1e6)
