const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

// 첫 줄
const n = parseInt(input[0]);

const Arr = [0, ...input[1].split(" ").map(Number)];

const start = parseInt(input[2]);

const visited = Array(n + 1).fill(false);

function dfs(start) {
  if (start > n || start <= 0) return false;
  if (!visited[start]) {
    visited[start] = true;
    dfs(start + Arr[start]);
    dfs(start - Arr[start]);
  }
  return true;
}

dfs(start);
console.log(visited.filter((e) => e === true).length);
