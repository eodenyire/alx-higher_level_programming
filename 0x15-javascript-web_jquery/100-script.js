#!/usr/bin/env node
/**
 * Script that updates the text color of the <header> element to red (#FF0000)
 * It uses document.querySelector to select the HTML tag
 * The script should be imported from the <head> tag, not at the end of the HTML
 */

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});

