#!/usr/bin/node
const intArg = parseInt(process.argv[2]);
if (isNaN(intArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + intArg);
}
