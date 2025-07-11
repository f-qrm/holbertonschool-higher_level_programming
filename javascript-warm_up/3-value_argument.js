#!/usr/bin/node
const args = process.argv[2];
if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
