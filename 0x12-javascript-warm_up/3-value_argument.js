#!/usr/bin/node

const args = process.argv;
let len;

for (const x of args) {
  len++;
}

if (len < 3) {
  console.log('No argument');
} else {
  console.log(args[3]);
}
