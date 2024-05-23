#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const charUrls = JSON.parse(body).characters;

    charUrls.forEach(charUrl => {
      request.get(charUrl, (charError, charResp, charBody) => {
        if (charError) {
          console.log(charError);
          return;
        }

        if (charResp.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  }
});
