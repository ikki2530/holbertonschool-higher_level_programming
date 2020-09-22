#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');
const myArgs = process.argv.slice(2);

const url = myArgs[0];
const file = myArgs[1];

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
