#!/usr/bin/node
// executes x times a function.

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
};
