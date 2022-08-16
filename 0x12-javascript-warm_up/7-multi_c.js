#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < times; x++) {
    console.log('C is fun');
  }
}
