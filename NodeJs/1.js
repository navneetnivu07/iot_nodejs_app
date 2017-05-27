// Nivu

var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://192.168.1.16')
var html;
var http = require('http');

 
client.on('connect', function () {
  client.subscribe('dead')
  client.publish('dead', 'Hello mqtt****')
})
 
client.on('message', function (topic, message) {
  // message is Buffer 
  console.log(message.toString())
  html += message.toString();
  client.end()
})

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});

  html = '<!DOCTYPE html><html><head><title>My Title</title></head><body>';
    html += 'Some more static content';
    html += 'Some more static content';
    html += 'Some more static content';
    html += 'Some dynamic content';
    html += '</body></html>';

    res.end(html, 'utf-8');
}).listen(8080, '192.168.1.16');