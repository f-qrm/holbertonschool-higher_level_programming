#!/usr/bin/node
function factorial (n) {
  if (isNaN(arg) || n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
const result = factorial(arg);

console.log(result);
