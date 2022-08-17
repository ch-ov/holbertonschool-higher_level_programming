#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let x = 0; x < list.length; x++) {
    reverse[list.length - x - 1] = list[x];
  }
  return reverse;
};
