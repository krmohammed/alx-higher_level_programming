#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (films) {
    $.each(films.results, function (i, film) {
      $('ul#list_movies').append(`<li>${film.title}</li>`)
    })
  }
})
