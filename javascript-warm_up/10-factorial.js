#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
