#!/usr/bin/node
// prints the addition of 2 integers
const myArgs = process.argv.slice(2);

if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < myArgs.length; i++) {
    myArgs[i] = parseInt(myArgs[i]);
  }

  let mx = myArgs[0];
  let secondMx = myArgs[0];
  for (let j = 1; j < myArgs.length; j++) {
    if (myArgs[j] > mx) {
      secondMx = mx;
      mx = myArgs[j];
    } else if (myArgs[j] > secondMx) {
      if (myArgs[j] !== mx) {
        secondMx = myArgs[j];
      }
    }
  }
  console.log(secondMx);
}
