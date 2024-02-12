#!/usr/bin/node

const args = process.argv;

if (len(args) == 3) {
  console.log('Argument found');
} else if (len(args) > 3){
  console.log('Arguments found');
} else {
  console.log('No argument');
}
