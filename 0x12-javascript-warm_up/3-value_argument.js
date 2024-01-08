#!/usr/bin/node

const args = process.argv;
let len = 0;

if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
