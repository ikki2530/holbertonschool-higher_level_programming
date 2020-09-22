#!/usr/bin/node
const fs = require('fs');

const myArgs = process.argv.slice(2);

const fileA = myArgs[0];
const fileB = myArgs[1];
const fileC = myArgs[2];

const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, dataA);
fs.appendFile(fileC, dataB, function (err) {
  if (err) throw err;
});
