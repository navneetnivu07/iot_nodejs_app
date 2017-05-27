load('api_config.js');
load('api_gpio.js');
load('api_mqtt.js');
load('api_sys.js');
load('api_timer.js');

// Helper C function get_led_gpio_pin() in src/main.c returns built-in LED GPIO
let pin = ffi('int get_led_gpio_pin()')();

// Blink built-in LED every second
GPIO.set_mode(pin, GPIO.MODE_OUTPUT);
MQTT.sub('control/n1', function(conn, topic, msg) {
  
    let pub_topic = 'devices/' + Cfg.get('device.id');
    let data = msg;
    let value = GPIO.write(pin, data);
    let ok = MQTT.pub(pub_topic, JSON.stringify({ pin: GPIO.read(pin)}), 1);
    print('Published:', ok ? 'yes' : 'no', 'topic:', pub_topic, 'pin status:', GPIO.read(pin));

}, null);
