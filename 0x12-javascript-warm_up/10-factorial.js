#!/usr/bin/node

function factorial (i) {
  return i === 0 || isNaN(i) ? 1 : i * factorial(i - 1);
}
console.log(factorial(Number(process.argv[2])));
