const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "ex.txt")
  .toString()
  .trim()
  .split("\n");

let answer = "";
for (let i = 2; i < input.length; i += 2) {
  answer += calc(i) + "\n";
}
console.log(answer);

function calc(i) {
  let stockFlow = input[i].split(" ").map(Number); // 가격들 배열
  let profit = 0;
  let maxPrice = 0;
  for (let j = stockFlow.length - 1; j >= 0; j--) {
    // 가격 뒤에서 부터 확인
    if (stockFlow[j] > maxPrice) {
      maxPrice = stockFlow[j];
    } // 제일 비싼 가격을 찾음
    profit += maxPrice - stockFlow[j];
  }
  return profit;
}
//출처: https://oesnuj.tistory.com/entry/Nodejs-백준-Javascript-11501-주식 [비트로 그리는 성장일기:티스토리]
// 배열을 역으로 순회하면 그냥 뒤에서 부터 최댓값을 구한다
// 순회 중에 현재까지의 가장 비싼 주가가 남는다
// 이 가격보다 비싸게 파는 날을 만나기 전까지는 모두 현재까지의 최대 가격으로 팔아주면 최고 익절이다

//댑악,, 이걸 어케 생각함.....
