#!/usr/bin/node
/* returns the reversed version of a list */

exports.esrever = function (list) {
  const rev = [];
  const lg = list.length;
  for (let i = lg - 1; i >= 0; i--) {
    rev.push(list[i]);
  }

  return rev;
};
