#!/usr/bin/node
/* prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const myArgs = process.argv.slice(2);

const find_id = '18';
const urlId = myArgs[0] + '/18';
request.get(urlId, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});