#!/usr/bin/node
/* imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */

const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  const ocurrences = dict[key];
  if (!newDict[ocurrences]) {
    newDict[ocurrences] = [];
  }
  newDict[ocurrences].push(key);
}
console.log(newDict);
