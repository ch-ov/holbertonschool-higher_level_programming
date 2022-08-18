#!/usr/bin/node
const fs = require('fs');
const test = process.argv[2];
fs.readFile(test, 'utf8', function (err, file) {
  if (err) {
    console.log(err);
  } else {
    console.log(file);
  }
});
