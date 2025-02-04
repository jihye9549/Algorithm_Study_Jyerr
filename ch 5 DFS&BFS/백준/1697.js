const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input[0].split(" ").map(Number);
const ch = new Array(100001).fill(0);
let cnt = 0;
function bfs(n) {
  if (n)
    for (const d of [n * 2, n + 1, n - 1]) {
    }
}

console.log(bfs(N));
