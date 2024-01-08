#!/usr/bin/node

const args = process.argv;
const first = Number(args[1]);
const second = Number(args[2]);

function add (a, b) {
  console.log(a + b);
}

add(first, second);
