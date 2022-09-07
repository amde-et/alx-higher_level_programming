#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  list.forEach(element => {
    if (element === searchElement) total++;
  });
  return total;
};
