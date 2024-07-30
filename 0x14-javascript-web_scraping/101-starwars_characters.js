#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, _, body) => {
  if (error) return console.error(error);
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) return;
  request(characters[index], (err, __, bdy) => {
    if (err) return console.error(err);
    console.log(JSON.parse(bdy).name);
    printCharacters(characters, index + 1);
  });
}
