function sameFrequency(num1, num2) {
  const n1 = num1.toString();
  const n2 = num2.toString();
  if (n1.length !== n2.length) return false;

  numObj1 = {};

  for (const char of n1) {
    numObj1[char] = (numObj1[char] || 0) + 1;
  }

  console.log(numObj1);

  for (const char of n2) {
    if (!numObj1[char]) return false;
    numObj1[char] -= 1;
  }

  return true;
}

// console.log(sameFrequency(182, 283)); //true
console.log(sameFrequency(3589578, 5879385)); //true
