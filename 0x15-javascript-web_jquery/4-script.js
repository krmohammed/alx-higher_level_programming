#!/usr/bin/node

$('div#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').toggleClass('red').addClass('green');
  }
})
