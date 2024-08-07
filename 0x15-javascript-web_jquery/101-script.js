#!/usr/bin/env node
/**
 * Script to handle adding, removing, and clearing items from a list using jQuery
 * - Adds a new <li> element to UL.my_list when DIV#add_item is clicked
 * - Removes the last <li> element from UL.my_list when DIV#remove_item is clicked
 * - Clears all <li> elements from UL.my_list when DIV#clear_list is clicked
 * This script must be imported from the <head> tag
 */

$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('.my_list li').last().remove();
  });

  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});

