#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const resData = JSON.parse(body);
    const result = {};
    for (let i = 0; i < resData.length; i++) {
      if (resData[i].completed === true) {
        if (!(resData[i].userId in result)) {
          result[resData[i].userId] = 0;
	}
        result[resData[i].userId] += 1;
      }
    }
    console.log(result);
  }
});
