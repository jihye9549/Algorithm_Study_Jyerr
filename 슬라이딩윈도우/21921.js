const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

const [n, x] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

let curV = 0; // 현재 값
let maxV = 0; // 최대 값
let maxC = 0; // 최대 값의 카운트

for (let i = 0; i < n - x + 1; i++) {
  if (i === 0) {
    for (let j = 0; j <= x - 1; j++) {
      curV += arr[j];
    }
    maxV = curV;
    maxC = 1;
  } else {
    curV = curV - arr[i - 1] + arr[i + x - 1];
    if (curV == maxV) {
      maxC += 1;
    } else if (curV > maxV) {
      maxV = curV;
      maxC = 1;
    }
  }
}

console.log(maxV == 0 ? "SAD" : maxV);

if (maxV !== 0) {
  console.log(maxC);
}
