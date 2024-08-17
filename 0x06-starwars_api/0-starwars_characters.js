#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

// Set up the options for the API request
const categories = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

// Make the initial request to get the movie details
request(categories, function (error, response, body) {
  if (error) {
    console.error('Failed to fetch movie details:', error);
    return;
  }

  try {
    const characters = JSON.parse(body).characters;

    // Check if characters array is valid and not empty
    if (!characters || characters.length === 0) {
      console.error('No characters found in the API response.');
      return;
    }

    // Start printing characters
    printCharacters(characters, 0);
  } catch (err) {
    console.error('Failed to parse movie details:', err);
  }
});

// Function to print characters recursively
function printCharacters (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error('Failed to fetch character data:', error);
      return;
    }

    try {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    } catch (err) {
      console.error('Failed to parse character data:', err);
    }
  });
}

