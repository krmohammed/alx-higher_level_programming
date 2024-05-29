#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  success: function (response) {
    $('div#character').text(response.name);
  }
})
