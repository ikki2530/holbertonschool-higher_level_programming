#!/usr/bin/node
/* computes the number of tasks completed by user id. */
const request = require('request');
const myArgs = process.argv.slice(2);

const url = myArgs[0];
request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const newDict = {};
  const listDict = JSON.parse(body);
  for (let i = 0; i < listDict.length; i++) {
    // console.log(listDict[i]);
    const newId = listDict[i].userId;
    if (listDict[i].completed === true && !newDict[newId]) {
      newDict[newId] = 1;
    } else if (listDict[i].completed === false) {
      continue;
    } else {
      newDict[newId] += 1;
    }
  }

  console.log(newDict);
});
