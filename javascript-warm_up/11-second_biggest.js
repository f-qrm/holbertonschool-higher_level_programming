#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  const max = sorted[0];

  let secondBiggest = 0;
  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] < max) {
      secondBiggest = sorted[i];
      break;
    }
  }
  console.log(secondBiggest);
}
