#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl + process.argv[2], (error, _, body) => {
  if (error) return console.error(error);

  JSON.parse(body).characters.forEach(url => {
    request(url, (err, __, bdy) => {
      if (err) return console.error(err);
      console.log(JSON.parse(bdy).name);
    });
  });
});
