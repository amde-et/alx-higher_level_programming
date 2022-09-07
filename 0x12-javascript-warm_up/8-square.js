#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let r = '';
    for (let c = 0; c < size; c++) r += 'X';
    console.log(r);
  }
}
