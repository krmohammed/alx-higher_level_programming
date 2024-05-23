#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const stringData = process.argv[3];

fs.writeFile(filePath, stringData, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
});
