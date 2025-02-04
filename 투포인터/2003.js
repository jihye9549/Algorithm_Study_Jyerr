const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const array = input[1].split(" ").map(Number);

let start = 0;
let end = 0;
let sum = 0;
let count = 0;

while (end <= n) {
  if (sum === m) {
    count++;
    sum -= array[start];
    start++;
  } else if (sum > m) {
    sum -= array[start];
    start++;
  } else {
    sum += array[end];
    end++;
  }
}

console.log(count);
 