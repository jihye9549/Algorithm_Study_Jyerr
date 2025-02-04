const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

// 첫 줄 노드 수
const N = parseInt(input[0]);

// 그래프 인접 리스트 (트리)
const Arr = Array.from({ length: N + 1 }, () => []);
const ResultArr = Array(N + 1).fill(0); // 부모 노드 저장

// 입력값을 기반으로 트리 구성
let index = 1;
for (let i = 1; i < N; i++) {
  const [a, b] = input[index++].split(" ").map(Number);
  Arr[a].push(b);
  Arr[b].push(a);
}

// 방문 여부 체크
const visited = Array(N + 1).fill(false);

function dfs(node) {
  visited[node] = true; // 방문 처리

  for (const next of Arr[node]) {
    if (!visited[next]) {
      ResultArr[next] = node; // 부모 노드 저장
      dfs(next);
    }
  }
}

// 루트 노드(1)부터 DFS 실행
dfs(1);

// 결과 출력 (2번 노드부터 부모 정보 출력)
console.log(ResultArr.slice(2).join("\n"));
