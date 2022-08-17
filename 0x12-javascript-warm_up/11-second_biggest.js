#!/usr/bin/node
const process = require('process');
const copy = [];
const args = process.argv;

for (let x = 2; x < args.length; x++) {
  copy.push(parseInt(args[x]));
}
copy.splice(copy.indexOf(Math.max(...copy)), 1);
if (copy.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...copy));
}
