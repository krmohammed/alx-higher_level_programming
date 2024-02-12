#!/usr/bin/node

const args = process.argv;
const first = Number(args[2]);

if (first) {
  console.log(`My number: ${first}`);
} else {
  console.log('Not a number');
}
