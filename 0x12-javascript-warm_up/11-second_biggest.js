#!/usr/bin/node

const args = process.argv;
let temp = [];

if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 2, j = 0; i < args.length; i++) {
    temp[j] = Number(args[i]);
    j++;
  }
  temp.sort((a, b) => b - a);
  console.log(temp[1]);
}
