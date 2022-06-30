function isSubsequence(w1, w2) {
  let j = 0;
  for (let i = 0; i < w2.length; i++) {
    if (w1[j] === w2[i]) {
      j++;
    }
    if (j === w1.length) return true;
  }
  return false;
}

// console.log(isSubsequence("hello", "hello world"));
// console.log(isSubsequence("sing", "sting"));
// console.log(isSubsequence("abc", "acb"));
