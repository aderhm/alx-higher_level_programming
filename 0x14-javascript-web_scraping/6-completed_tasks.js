#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const resData = JSON.parse(body);
    for (let i = 0; i < resData.length; i++) {
      if (resData[i].completed === true) {
        console.log(resData[i]);
      }
    }
  }
});
