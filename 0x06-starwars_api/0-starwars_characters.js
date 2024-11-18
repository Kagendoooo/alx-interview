#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error fetching film data: ${error}`);
    return;
  }

  let filmData;
  try {
    filmData = JSON.parse(body);
  } catch (parseError) {
    console.error('Error parsing film data:', parseError);
    return;
  }

  const characters = filmData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  function fetchCharacter(index) {
    if (index >= characters.length) return;

    request(characters[index], (err, res, characterBody) => {
      if (err) {
        console.error(`Error fetching character data: ${err}`);
        return;
      }

      let characterData;
      try {
        characterData = JSON.parse(characterBody);
      } catch (parseError) {
        console.error('Error parsing character data:', parseError);
        return;
      }

      console.log(characterData.name);

      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
