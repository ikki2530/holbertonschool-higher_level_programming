#!/usr/bin/node
/* reads and prints the content of a file. */
const fs = require('fs');
const myArgs = process.argv.slice(2);


  
// fs.readFile(myArgs[0], (err, data) => {
//   try {
//     console.log(data.toString()); 
//   } catch (err) {
//     console.log(err);
//   }

// }) 

// try {
//   const dataA = fs.readFileSync(myArgs[0], 'utf8');
//   console.log(dataA);
// }
// catch (err) {
//   console.log(err);
// }

try {
  fs.readFile(myArgs[0], (err, data) => {
    if (err) {
      throw err;
    }
    console.log(data.toString());
  })
} catch (ex) {
  console.log(ex)
}