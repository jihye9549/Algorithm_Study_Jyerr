const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
let input = require("fs").readFileSync(filePath).toString().trim().split("\n");
const n = parseInt(input[0], 10);
const arr = [0, ...input.slice(1).map(Number)];

const dp = new Array(n + 1);

dp[1] = arr[1]; //6
dp[2] = arr[1] + arr[2]; //16
dp[3] = Math.max(dp[1] + arr[3], dp[2], arr[2] + arr[3]);

for (let i = 4; i <= n; i++) {
  dp[i] = Math.max(
    dp[i - 2] + arr[i],
    dp[i - 1],
    dp[i - 3] + arr[i - 1] + arr[i]
  );
}

console.log(dp[n]);
