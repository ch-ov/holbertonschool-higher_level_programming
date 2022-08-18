#!/usr/bin/node
const request = require('request');
const test = process.argv[2];
request(test, function (err, response) {
  if (err) throw err;
  console.log('code:', response.statusCode);
});
