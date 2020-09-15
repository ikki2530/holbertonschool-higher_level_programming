#!/usr/bin/node
// prints a square
const myArgs = process.argv.slice(2);
let square = '';
if (isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(myArgs[0]); i++) {
    for (let j = 0; j < parseInt(myArgs[0]); j++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
}
