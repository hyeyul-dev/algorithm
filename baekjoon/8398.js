// n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

const fs = require("fs");
let input = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3`
).trim();

const number = parseInt(input);
let answer = 0;
for (let i = 1; i <= number; i++) {
  answer += i;
}

console.log(answer);