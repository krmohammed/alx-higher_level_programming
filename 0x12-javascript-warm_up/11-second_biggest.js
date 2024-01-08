#!/usr/bin/node

function second_biggest (array) {
  const temp = [];

  if (array.length === 2 || array.length === 3) {
    return (0);
  }

  array.forEach((n) => {
    num = Number(n);
    if (num) {
      temp.push(num);
    }
  });

  temp.sort();
  return (temp[temp.length - 2]);
}

const sec_big = second_biggest(process.argv);
console.log(sec_big);
