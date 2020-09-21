#!/usr/bin/node
/* class Square inherits */
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let ch = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          ch += c;
        }
        console.log(ch);
        ch = '';
      }
    }
  }
}

module.exports = Square;
