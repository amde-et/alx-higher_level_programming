#!/usr/bin/node

const arg = process.argv[2];
console.log(typeof arg === 'undefined' ? 'No argument' : arg);

