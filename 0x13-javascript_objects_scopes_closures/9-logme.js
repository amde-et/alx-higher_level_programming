#!/usr/bin/node

let total = 0;
exports.logMe = function (item) {
  console.log(`${total++}: ${item}`);
};
