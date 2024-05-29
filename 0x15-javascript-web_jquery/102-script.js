#!/usr/bin/node

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const a = $('input#language_code').val();
    let myUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${a}`;
    $.ajax({
      type: 'GET',
      url: myUrl,
      success: function (response) {
        $('div#hello').text(response.hello);
      }
    })
  })
})
