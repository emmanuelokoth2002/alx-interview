#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

if (!movieID) {
  console.error('Please provide a Movie ID.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieID}/`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach((characterURL) => {
      request(characterURL, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('Failed to fetch character:', error);
        }
      });
    });
  } else {
    console.error('Failed to fetch movie data:', error);
  }
});
