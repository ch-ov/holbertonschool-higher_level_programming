#!/usr/bin/node
function factorial (intOne) {
  if (isNaN(intOne) || intOne === 0) {
    return 1;
  } else {
    return intOne * factorial(intOne - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
