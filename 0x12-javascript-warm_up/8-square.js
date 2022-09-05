#!/usr/bin/node
const argument = parseInt(process.argv[2]);
let string = '';
if (Number.isNaN(argument)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < argument; x++) {
    for (let y = 0; y < argument; y++) {
      string += 'X';
    }
    string += '\n';
  }
  console.log(string);
}
