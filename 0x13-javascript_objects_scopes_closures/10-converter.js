#!/usr/bin/node
exports.converter = function (base) {
  function converts (number) {
    return number.toString(base);
  }
  return converts;
};
