#!/usr/bin/node
const argv1 = parseInt(process.argv[2]);
const argv2 = parseInt(process.argv[3]);

if (isNaN(argv1 || argv2)) {
  console.log(NaN);
} else {
  console.log(argv1 + argv2);
}
