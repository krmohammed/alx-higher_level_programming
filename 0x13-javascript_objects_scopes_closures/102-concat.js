#!/usr/bin/node

const fs = require('fs');

function concatFiles (file1, file2, destination) {
  const dataFile1 = fs.readFileSync(file1, 'utf-8');
  const dataFile2 = fs.readFileSync(file2, 'utf-8');
  const concatenatedData = `${dataFile1}${dataFile2}`;
  fs.writeFileSync(destination, concatenatedData);
}
const args = process.argv;
concatFiles(args[2], args[3], args[4]);
