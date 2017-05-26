import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("192.168.1.16", 1883, 60)
client.loop_start()

while True:
    temperature = 1
    client.publish("devices/1", temperature)
    print "hi"
    time.sleep(5)
