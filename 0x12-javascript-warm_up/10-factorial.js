#!/usr/bin/node
// prints the addition of 2 integers
const myArgs = process.argv.slice(2);

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    num = num * factorial(num - 1);
  }
  return num;
}

const number = parseInt(myArgs[0]);
const result = factorial(number);
console.log(result);
