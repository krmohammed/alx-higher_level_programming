#!/usr/bin/node

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (resp) {
      $('div#hello').text(resp.hello);
    }
  })
})
