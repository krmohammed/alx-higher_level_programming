#!/usr/bin/node

const args = process.argv;
const temp = [];

args.forEach((n) => {
  temp.push(n);
});

temp.sort();
console.log(temp[temp.length - 2]);
