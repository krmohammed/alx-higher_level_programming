#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let areaStr = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          areaStr += c;
        }
        if (this.height - i > 1) {
          areaStr += '\n';
        }
      }
      console.log(areaStr);
    } else {
      super.print();
    }
  }
};