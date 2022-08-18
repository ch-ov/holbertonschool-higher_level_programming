#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const aux = {};
    const json = JSON.parse(body);
    for (let x = 0; x < json.length; x++) {
      if (json[x].completed === true) {
        if (aux[json[x].userId] === undefined) {
          aux[json[x].userId] = 0;
        }
        aux[json[x].userId]++;
      }
    }
    console.log(aux);
  }
});
