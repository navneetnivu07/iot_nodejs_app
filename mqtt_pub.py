import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("192.168.1.16", 1883, 60)
client.loop_start()

while True:
	client.publish("control/n1", i)

	send_msg = {
	        'pin': d1,
	        'status': 0
	}

	client.publish("control/n1", payload=json.dumps(send_msg), qos=2, retain=False)
	time.sleep(5000)

		
