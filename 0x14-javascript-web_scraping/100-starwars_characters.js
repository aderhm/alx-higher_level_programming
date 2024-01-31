#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
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
