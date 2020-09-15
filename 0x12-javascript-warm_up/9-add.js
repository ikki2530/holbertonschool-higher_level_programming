#!/usr/bin/node
// prints the addition of 2 integers
const myArgs = process.argv.slice(2);

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(myArgs[0], myArgs[1]);
