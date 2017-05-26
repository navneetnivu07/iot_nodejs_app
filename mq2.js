var mqtt = require('mqtt'), url = require('url');
// Parse 
var mqtt_url = url.parse(process.env.CLOUDMQTT_URL || '192.168.1.16:1883');
var auth = (mqtt_url.auth || ':').split(':');
var url = "mqtt://" + mqtt_url.host;

var options = {
  port: mqtt_url.port,
  clientId: 'mqttjs_' + Math.random().toString(16).substr(2, 8),

};

// Create a client connection
var client = mqtt.connect(url, options);

client.on('connect', function() { // When connected

  // subscribe to a topic
  client.subscribe('dead', function() {
    // when a message arrives, do something with it
    client.on('message', function(topic, message, packet) {
      console.log("Received '" + message + "' on '" + topic + "'");
    });
  });

  // publish a message to a topic
  client.publish('dead', 'my message', function() {
    console.log("Message is published");
    client.end(); // Close the connection when published
  });
});