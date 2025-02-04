const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

// 첫 번째 줄 처리
const [N, M, V] = input[0].split(" ").map(Number);

// 간선 정보 처리
let edges = Array.from({ length: N + 1 }, () => []);
for (let i = 1; i <= M; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  edges[a].push(b);
}

edges = edges.map((edge) => edge.sort((a, b) => a - b));

let visitedDfs = Array(N + 1).fill(false);
let visitedBfs = [];
let r = [];
let needVisitBfs = [];
function dfs(v) {
  visitedDfs[v] = true;
  r.push(v);
  for (let i of edges[v]) {
    if (!visitedDfs[i]) {
      dfs(i);
    }
  }
}
function bfs(v) {
  needVisitBfs.push(v);

  while (needVisitBfs.length !== 0) {
    const node = needVisitBfs.shift();
    if (!visitedBfs.includes(node)) {
      visitedBfs.push(node);
      needVisitBfs = [...needVisitBfs, ...edges[node]];
    }
  }
  return visitedBfs;
}
dfs(V);
console.log(r);
console.log(bfs(V));
