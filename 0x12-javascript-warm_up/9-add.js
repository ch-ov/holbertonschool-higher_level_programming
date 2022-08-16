#!/usr/bin/node
const intOne = parseInt(process.argv[2]);
const intTwo = parseInt(process.argv[3]);
function add (x, y) {
  if (isNaN(x) || isNaN(y)) {
    return NaN;
  }
  return x + y;
}
console.log(add(intOne, intTwo));
