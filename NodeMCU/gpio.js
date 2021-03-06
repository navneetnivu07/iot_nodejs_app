load('api_config.js');
load('api_gpio.js');
load('api_mqtt.js');
load('api_sys.js');
load('api_timer.js');

// Helper C function get_led_gpio_pin() in src/main.c returns built-in LED GPIO
let d4 = ffi('int get_led_gpio_pin()')(); // GPIO2 : D4
let d1 = 5; // GPIO5 : D1
let d2 = 4; // GPIO4 : D2

// Blink built-in LED every second
GPIO.set_mode(d4, GPIO.MODE_OUTPUT);
GPIO.set_mode(d1, GPIO.MODE_OUTPUT);
GPIO.set_mode(d2, GPIO.MODE_OUTPUT);


MQTT.sub('control/n1', function(conn, topic, msg) {
  
    let pub_topic = 'devices/' + Cfg.get('device.id');
    if(msg === "0"){
      GPIO.write(d4, 0);
      GPIO.write(d1, 0);
      GPIO.write(d2, 0);

    } else if(msg === "1"){
      GPIO.write(d4, 1);
      GPIO.write(d1, 1);
      GPIO.write(d2, 1);

    }
    let ok = MQTT.pub(pub_topic, JSON.stringify({ pin: GPIO.read(d4)}), 1);
    print('Published:', ok ? 'yes' : 'no', 'topic:', pub_topic, 'pin status:', GPIO.read(d4));
    print('pin status: D1 : ', GPIO.read(d1), ' D2 : ', GPIO.read(d2), ' D4 : ', GPIO.read(d4));

}, null);
