//https://no2jfamily.tistory.com/m/62
// 브루트포스 알고리즘
// 백트래킹

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .split("\n");

const n = +input.shift();
const array = input.shift().split(" ").map(Number); //[5, 6]이 들어가있을것
const operators = input.shift().split(" ").map(Number); // [0 0 1 0]

let max = -Infinity;
let min = +Infinity;

//함수도 일종의 객체이기 때문에 배열의 요소로 사용가능
const calculate = [
  (a, b) => a + b,
  (a, b) => a - b,
  (a, b) => a * b,
  (a, b) => ~~(a / b),
];

const dfs = (count, result) => {
  if (count === n - 1) {
    max = Math.max(max, result);
    min = Math.min(min, result);
    return; // <-- 필요
  }
  for (let i = 0; i < 4; i++) {
    //연산자는 4개로 고정이므로 범위를 N까지로 설정하면 안됌
    if (!operators[i]) continue;
    operators[i]--;
    dfs(count + 1, calculate[i](result, array[count + 1]));
    operators[i]++;
  }
};

dfs(0, array[0]); //dfs(0, 5) 호출
console.log(max);
console.log(min);
