import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  

def my_callback(channel):  
    print "Rising edge detected on port 24 - even though, in the main thread,"  
    print "we are still waiting for a falling edge - how cool?\n"  
  
def handle(pin):
	print pin
	#GPIO.output(LED_B, not GPIO.input(BTN_B))
 


#GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)  
  
try:  
    print "Waiting for falling edge on port 23"  
    GPIO.add_event_detect(23, GPIO.BOTH, handle)
    print "Falling edge detected. Here endeth the second lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
