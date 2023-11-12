#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (err, res, body) => {
  if (err) console.log(err);
  const index = 0;
  const characters = JSON.parse(body).characters;
  displayName(characters, index);
});

const displayName = function (url, index) {
  request(url[index], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++index < url.length) {
      displayName(url, index++);
    }
  });
};
