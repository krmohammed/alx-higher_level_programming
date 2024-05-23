#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const users = JSON.parse(body);
    const activeUsers = users.filter(user => user.completed === true);
    const completed = {};

    activeUsers.forEach(user => {
      if (completed[user.userId]) {
        completed[user.userId]++;
      } else {
        completed[user.userId] = 1;
      }
    });
  }
});
