#!/usr/bin/node

const args = process.argv;
const first = Number(args[2]);
const second = Number(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(first, second);
