#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < squareSize; x++) {
    console.log('X'.repeat(squareSize));
  }
}
