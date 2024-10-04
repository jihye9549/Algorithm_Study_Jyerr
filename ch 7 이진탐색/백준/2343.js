const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const array = input[1].split(" ").map(Number);

let start = Math.max(...array); // 최적의 구간 합의 최소값은 배열의 최대값이어야 함
let end = array.reduce((acc, cur) => acc + cur, 0); // 최적의 구간 합의 최대값은 배열의 전체 합이어야 함

let result = end;

while (start <= end) {
  let mid = Math.floor((start + end) / 2);

  let sum = 0;
  let count = 1;

  array.forEach((el, i) => {
    if (sum + el > mid) {
      sum = 0;
      count += 1;
    }
    sum += el;
  });

  if (count > m) {
    start = mid + 1;
  } else {
    result = mid; // 가능한 경우, 결과를 업데이트하고 더 작은 용량을 시도
    end = mid - 1;
  }
}

console.log(result);
