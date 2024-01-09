#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let areaStr = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        areaStr += 'X';
      }
      if (this.height - i > 1) {
        areaStr += '\n';
      }
    }
    console.log(areaStr);
  }
};
