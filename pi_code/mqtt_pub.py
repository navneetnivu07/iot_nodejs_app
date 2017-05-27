import paho.mqtt.client as mqtt
import time
import json
import requests

url = 'http://livemonitoring.info/node/ins.php'
headers = {'content-type': 'application/json'}

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("devices/status/#")

def on_message(client, userdata, msg):
    print("1" + msg.topic+" "+str(msg.payload))
    response = requests.post(url, data=json.dumps(msg.payload), headers=headers)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('ant', 'antWARE#5747')
client.connect("192.168.1.16", 1883, 60)
client.loop_start()

MQTT_MSG_OFF=json.dumps({"pin":2,"action":0})
MQTT_MSG_ON=json.dumps({"pin":2,"action":1})
i=0

while True:
	#client.publish("control/n1", payload=json.dumps(send_msg), qos=2, retain=False)
	if i%2 == 0:
		client.publish("control/n4", MQTT_MSG_OFF)
	else:
		client.publish("control/n4", MQTT_MSG_ON)
	i += 1
	print(i)
	time.sleep(5)
