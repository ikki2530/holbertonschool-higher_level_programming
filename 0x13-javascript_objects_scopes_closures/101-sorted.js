#!/usr/bin/node
/* imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */

const dict = require('./101-data').dict;

new_dict = {}
for (var key in dict) {
  let ocurrences = dict[key];
  if (!new_dict[ocurrences]) {
      new_dict[ocurrences] = []; 
  }
  new_dict[ocurrences].push(key);
}
console.log(new_dict);
