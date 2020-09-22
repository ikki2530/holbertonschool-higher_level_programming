#!/usr/bin/node
/* request GET */
const request = require('request');
const myArgs = process.argv.slice(2);

request.get(myArgs[0], (err, res, body) => {
  if (err) {
    return console.log("code: " + err);
  }
  console.log("code: " + res.statusCode);
});
