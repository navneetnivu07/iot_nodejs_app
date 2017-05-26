// garage.js
const mqtt = require('mqtt')  
const client = mqtt.connect('mqtt://broker.hivemq.com')

/**
* The state of the garage, defaults to closed
* Possible states : closed, opening, open, closing
*/

var state = 'closed'

client.on('connect', () => {  
  // Inform controllers that garage is connected
  client.publish('garage/connected', 'true')
    sendStateUpdate()

})

// added to end of garage.js
function sendStateUpdate () {  
  console.log('sending state %s', state)
  client.publish('garage/state', state)
}