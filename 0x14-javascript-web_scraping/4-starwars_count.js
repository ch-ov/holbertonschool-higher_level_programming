#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const char in characters) {
        if (characters[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
