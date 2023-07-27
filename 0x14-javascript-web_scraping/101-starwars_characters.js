#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, { json: true }, (error, response, data) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = data.characters;
  const characterNames = [];
  const characterUrls = [...characters]; // To copy the array to preserve order

  // A function to fetch character data &  push the name in d correct order
  function fetchCharacterData () {
    const characterUrl = characterUrls.shift();
    if (!characterUrl) {
      // When all characters are processed, print the names
      console.log(characterNames.join('\n'));
      return;
    }

    request.get(characterUrl, { json: true }, (error, response, characterData) => {
      if (error) {
        console.error(error);
      } else {
        characterNames.push(characterData.name);
      }

      // Code  to fetch next character's data
      fetchCharacterData();
    });
  }

  // Code to start fetching the character data
  fetchCharacterData();
});
