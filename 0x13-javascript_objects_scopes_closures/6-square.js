#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    let areaStr = '';
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        areaStr += c;
      }
      if (this.height - i > 1) {
        areaStr += '\n';
      }
    }
    console.log(areaStr);
  }
};
