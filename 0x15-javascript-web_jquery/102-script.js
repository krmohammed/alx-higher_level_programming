#!/usr/bin/node

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const a = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/?lang=' + a,
      success: function (response) {
        $('div#hello').text(response.hello);
      }
    })
  })
})
