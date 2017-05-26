#!/usr/bin/env nodejs
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});

  var html = '<!DOCTYPE html><html><head><title>My Title</title></head><body>';
    html += 'Some more static content';
    html += 'Some more static content';
    html += 'Some more static content';
    html += 'Some dynamic content';
    html += '</body></html>';

    res.end(html, 'utf-8');
}).listen(8080, '192.168.1.16');
console.log('Server running at http://localhost:8080/');
