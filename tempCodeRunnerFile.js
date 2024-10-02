const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
let input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());

const arr = input.map(Number);
const d = new Array(n + 1);

d[1] = 1;
d[2] = 2;
d[3] = 4;

for (let i = 4; i <= arr[arr.length - 1]; i++) {
  d[i] = d[i - 1] + d[i - 2] + d[i - 3];
}

arr.forEach((el, i) => {
  //i 없으면 안돌아가
  console.log(d[el]);
});
