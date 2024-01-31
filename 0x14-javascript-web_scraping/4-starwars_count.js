#!/usr/bin/node
const request = require('request');
let numOfMovies = 0;
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const resBody = JSON.parse(body);
    const results = resBody.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          numOfMovies++;
        }
      }
    }
  }
  console.log(numOfMovies);
});
