#!/usr/bin/node

const total = process.argv.length;
console.log(total === 2 ? 'No argument' : total === 3 ? 'Argument found' : 'Arguments found');
