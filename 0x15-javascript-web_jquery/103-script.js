#!/usr/bin/node

$(document).ready(function () {
  function myFetch() {
    const a = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/?lang=' + a,
      success: function (response) {
        $('div#hello').text(response.hello);
      }
    })
  }

  $('input#btn_translate').click(myFetch);
  $('input#language_code').keypress(function (e) {
    if (e.keyCode == 13) {
      myFetch();
    }
  })
})
