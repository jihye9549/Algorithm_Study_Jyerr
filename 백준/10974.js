const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim();

const n = Number(input);
const check = new Array(n).fill(false);
const numA = Array.from({ length: n }, (value, index) => index + 1); // [1, 2, 3, ..., n]

let newA = [];

function dfs(k) {
  if (k === n) {
    console.log(newA.join(" "));
    return;
  }

  for (let i = 0; i < n; i++) {
    if (check[i]) continue; // 이미 방문한 숫자는 건너뜀
    check[i] = true; // 현재 숫자를 사용함으로 표시
    newA.push(numA[i]); // 현재 숫자를 결과 배열에 추가

    dfs(k + 1); // 다음 깊이로 이동

    check[i] = false; // 상태 복구: 현재 숫자를 사용하지 않음으로 표시
    newA.pop(); // 상태 복구: 배열에서 마지막에 추가한 숫자를 제거
  }
}

dfs(0);
