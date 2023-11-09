#!/usr/bin/node

const axios = require('axios');
const movieID = process.argv[2];

if (!movieID) {
  console.error('Please provide a Movie ID.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieID}/`;

axios.get(url)
  .then(response => {
    const filmData = response.data;
    const characters = filmData.characters;

    characters.forEach(characterURL => {
      axios.get(characterURL)
        .then(response => {
          console.log(response.data.name);
        })
        .catch(error => {
          console.error('Failed to fetch character:', error);
        });
    });
  })
  .catch(error => {
    console.error('Failed to fetch movie data:', error);
  });
