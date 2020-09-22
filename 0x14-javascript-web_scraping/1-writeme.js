#!/usr/bin/node
/* reads and prints the content of a file. */
const fs = require('fs');
const myArgs = process.argv.slice(2);

try {
  const file = myArgs[0];
  const cont = myArgs[1];
  fs.writeFileSync(file, cont);
} catch (err) {
  console.log(err);
}
