#!/usr/bin/env node
/**
 * Script to fetch and display how to say "Hello" in a specified language
 * - Fetches the translation based on the language code input from INPUT#language_code
 * - Displays the translation in the HTML tag DIV#hello
 * - Triggered when INPUT#btn_translate is clicked
 * This script must be imported from the <head> tag
 */

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});

