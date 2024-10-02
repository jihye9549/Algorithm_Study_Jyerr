const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
let input = require("fs").readFileSync(filePath).toString().trim().split("\n");
const n = input.map(Number).shift();
const dp = new Array(n + 1);

dp[1] = 1;
dp[2] = 2;
dp[3] = 3;

for (let i = 4; i <= n; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
}

console.log(dp[n] % 15746);
