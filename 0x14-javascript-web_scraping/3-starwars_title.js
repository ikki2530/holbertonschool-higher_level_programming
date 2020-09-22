#!/usr/bin/node
/* Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const myArgs = process.argv.slice(2);

request.get(myArgs[0], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body));
});