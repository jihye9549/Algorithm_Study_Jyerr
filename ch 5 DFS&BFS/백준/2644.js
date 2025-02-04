const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]); // 전체 사람의 수
const [personA, personB] = input[1].split(" ").map(Number); // 촌수를 계산할 두 사람의 번호
const m = Number(input[2]); // 부모 자식 관계의 개수

// 관계 저장을 위한 배열 초기화 (인덱스를 1부터 사용하기 위해 n + 1 크기 사용)
const relations = Array.from({ length: n + 1 }, () => []);

// 관계 입력 처리
for (let i = 3; i < 3 + m; i++) {
  const [parent, child] = input[i].split(" ").map(Number);
  relations[parent].push(child);
  relations[child].push(parent);
}

function bfs(start, target) {
  const visited = [];
  let needVisit = [[startNode, 0]];

  while (needVisit.length) {
    const [node, cnt] = needVisit.shift;
    if (node === target) return cnt;
    if (!visited.includes(node)) {
      visited.push(node);
      let nodes = graph[node].map((e) => [e, cnt + 1]);
      needVisit = [...needVisit, ...nodes];
    }
  }
}

console.log(bfs(personA, personB));
