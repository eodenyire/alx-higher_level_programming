#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, _, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    const movies = data.results.filter(film => film.characters.some(url => url.endsWith(`/${characterId}/`)));
    console.log(movies.length);
  }
});
