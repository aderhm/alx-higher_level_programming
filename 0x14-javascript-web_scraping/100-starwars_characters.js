#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const resData = JSON.parse(body);
    const characters = resData.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
