#!/usr/bin/node

const num = Number(process.argv[2])

function factorial (n) {
  if (!n) {
    return 1;
  }
  else {
    return n * factorial(n - 1);
  }
}

const facto = factorial(num);
console.log(facto);
