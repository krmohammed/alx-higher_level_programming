#!/usr/bin/node

function secondBiggest (array) {
  const temp = [];

  if (array.length === 2 || array.length === 3) {
    return (0);
  }

  array.forEach((n) => {
    const num = Number(n);
    if (num) {
      temp.push(num);
    }
  });

  temp.sort();
  return (temp[temp.length - 2]);
}

const secBig = secondBiggest(process.argv);
console.log(secBig);
