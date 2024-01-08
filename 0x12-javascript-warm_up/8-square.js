#!/usr/bin/node

const first = Number(process.argv[2]);
let square = '';

if (first) {
  for (let i = 0; i < first; i++) {
    for (let j = 0; j < first; j++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square);
} else {
  console.log('Missing size');
}
