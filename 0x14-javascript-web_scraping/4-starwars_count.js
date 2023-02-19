#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2]
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    let numMoviesWithWedge = 0;

    films.forEach((film) => {
      const characters = film.characters;
	    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        numMoviesWithWedge++;
      }
    });

    console.log(`${numMoviesWithWedge}`);
  }
});
