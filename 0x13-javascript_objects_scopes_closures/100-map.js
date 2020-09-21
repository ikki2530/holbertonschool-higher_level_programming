#!/usr/bin/node
/* imports an array and computes a new array. */

const list = require('./100-data').list;

const mp = list.map((x, index) => {
  return x * index;
});
console.log(list);
console.log(mp);
