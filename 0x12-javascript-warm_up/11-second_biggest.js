#!/usr/bin/node
// prints the addition of 2 integers
const myArgs = process.argv.slice(2);

if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 0; i < myArgs.length; i++) {
    arr.push(parseInt(myArgs[i], 10));
  }
  arr.sort((a, b) => a - b);
  arr.reverse();

  const mx = arr[0];
  for (let j = 0; j < arr.length; j++) {
    if (arr[j] < mx) {
      console.log(arr[j]);
      break;
    }
  }
}
