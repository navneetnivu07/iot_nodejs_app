import RPi.GPIO as GPIO

PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
i = 0

while True:
	GPIO.wait_for_edge(PIN, GPIO.RISING)
	print str(i) + " Rising"
	print "-------------------"
	i+=1
	GPIO.wait_for_edge(PIN, GPIO.FALLING)
	print str(i) + " Falling"
	print "-------------------"
	i+=1
