#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    return num.toString(base);
  }
  return convert;
};
