#!/usr/bin/node

const request = require('request');
const charId = 18;
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)).length;
    console.log(count);
  }
});
