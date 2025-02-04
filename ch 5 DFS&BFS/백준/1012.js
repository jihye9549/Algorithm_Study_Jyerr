const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

// 첫 줄: 테스트 케이스의 수
const T = parseInt(input[0]);

// 테스트 케이스 처리
let index = 1; // 현재 처리 중인 줄의 인덱스

for (let t = 0; t < T; t++) {
  let cnt = 0;
  // 각 테스트 케이스의 첫 줄
  const [M, N, K] = input[index++].split(" ").map(Number);

  // 배추밭 초기화 (N x M 크기 2차원 배열)
  const graph = Array.from({ length: N }, () => Array(M).fill(0));

  // 배추 위치 정보 저장
  for (let k = 0; k < K; k++) {
    const [X, Y] = input[index++].split(" ").map(Number);
    graph[Y][X] = 1; // X, Y 좌표에 배추 심기
  }
  const d = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
  ];

  function dfs(y, x) {
    if (x < 0 || x >= M || y < 0 || y >= N) return false;
    if (graph[y][x] === 1) {
      graph[y][x] = 0;
      // 4방향 탐색
      for (const [dy, dx] of d) {
        dfs(y + dy, x + dx);
      }
      return true;
    }
    return false;
  }

  for (let i = 0; i < N; i++) {
    // i가 행
    for (let j = 0; j < M; j++) {
      // j가 열
      if (dfs(i, j)) {
        cnt++;
      }
    }
  }

  console.log(cnt);
}
