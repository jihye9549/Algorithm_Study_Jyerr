const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map(Number);

const N = input[0];
const dp = new Array(N + 1);

dp[1] = input[1];
dp[2] = dp[1] + input[2];
dp[3] = Math.max(input[1], input[2]) + input[3];

// n개의 계단이 있을때 n-1계단을 밟았다고 가정하면, 세개 연속 밟을 수 없으므로 n-3도 무조건 밟았을 것이다.
// n개의 계단이 있을 때  n-2계단을 밟았다고 가정하면, 그 이전에 n-3, n-4 모두 밟을 수 있었지만 이건 이전 사이클에서 이미 계산되어n-2가 된 것이므로 고려하지 않는다.

for (let i = 4; i <= N; i++) {
  dp[i] = Math.max(dp[i - 3] + input[i - 1] + input[i], dp[i - 2] + input[i]);
}

console.log(dp[N]);
