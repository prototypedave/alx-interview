#!/usr/bin/node
/*  Star Wars Characters */
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
const movieId = process.argv[2];
/* request from api */
request(apiUrl + movieId, (error, response, body) => {
  if (error) throw error;
  const characters = JSON.parse(body).characters;
  showNames(characters);
});
/* display names */
const showNames = (names, i = 0) => {
  if (i === names.length) return;
  request(names[i], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    showNames(names, i + 1);
  });
};
