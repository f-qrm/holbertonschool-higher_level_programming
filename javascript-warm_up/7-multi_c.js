#!/usr/bin/node
const arg = process.argv[2];
const output = 'C is fun';

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(output);
  }
}
