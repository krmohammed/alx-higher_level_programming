#!/usr/bin/node

const fs = require('fs');
conast args = process.argv;

const contentA = fs.readFile(args[2], 'utf-8', (err) => {
  if (err) throw err;
});

const contentB = fs.readFile(args[3], 'utf-8', (err) => {
  if (err) throw err;
});

const concatenated = contentA + contentB;

fs.writeFile(args[4], concatenated, (err) => {
  if (err) throe err;
})
