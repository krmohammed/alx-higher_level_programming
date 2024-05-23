#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
    })
  }
});
