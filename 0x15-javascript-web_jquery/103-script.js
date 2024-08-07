#!/usr/bin/env node
/**
 * Script to fetch and display how to say "Hello" in a specified language
 * - Fetches the translation based on the language code input from INPUT#language_code
 * - Displays the translation in the HTML tag DIV#hello
 * - Triggered when INPUT#btn_translate is clicked or ENTER key is pressed
 * This script must be imported from the <head> tag
 */

$(document).ready(function () {
  function fetchHello() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key
      fetchHello();
    }
  });
});

