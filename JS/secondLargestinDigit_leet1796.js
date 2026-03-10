s = "abc1111"
let max = s[0];
let first = -Infinity;
let second = -Infinity;
for (let i of s) {
    // if i is a number
  if (!isNaN(i)) {
    if (i > first) {
      second = first;
      first = i;
    } else if (i > second && Number(i) != Number(first)) {
      second = i;
    }
  }
}
if (Number(first) === Number(second)) {
  console.log(-1);
} else {
  console.log(Number(second));
}
