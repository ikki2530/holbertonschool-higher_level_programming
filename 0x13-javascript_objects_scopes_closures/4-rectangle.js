#!/usr/bin/node
/* Empty class Rectangle */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
      rect = '';
    }
  }

  rotate() {
    let wd = this.width;
    this.width = this.height;
    this.height = wd;
  }

  double() {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
