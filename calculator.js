let num1 = 10;        // 첫 번째 숫자
let operator = "*";   // 연산자 (+, -, *, / 중 하나 입력)
let num2 = 5;         // 두 번째 숫자

let result = 0; // 결과를 저장할 변수

if (operator === '+') {
  result = num1 + num2;
} else if (operator === '-') {
  result = num1 - num2;
} else if (operator === '*') {
  result = num1 * num2;
} else if (operator === '/') {
  result = num1 / num2;
} else {
  console.log("잘못된 연산자입니다. +, -, *, / 중에서 입력해주세요.");
}

if (operator === '+' || operator === '-' || operator === '*' || operator === '/') {
  console.log("결과: " + num1 + " " + operator + " " + num2 + " = " + result);
}