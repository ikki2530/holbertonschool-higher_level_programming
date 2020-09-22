#!/usr/bin/node
/* prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const myArgs = process.argv.slice(2);

const findId = '18';
const url = myArgs[0];
let cont = 0;
request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const listDict = JSON.parse(body).results;
  for (let i = 0; i < listDict.length; i++) {
    // console.log(listDict[i].characters);
    for (let j = 0; j < listDict[i].characters.length; j++) {
      // check if in each url is id 18
      if (listDict[i].characters[j].includes(findId)) {
        cont += 1;
      }
    }
  }
  console.log(cont);
  // console.log(JSON.parse(body).results[0]);
});
