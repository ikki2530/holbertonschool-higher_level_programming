#!/usr/bin/node
/* Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const myArgs = process.argv.slice(2);

const urlId = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request.get(urlId, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
