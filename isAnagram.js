function isAnagram(val1, val2) {
  //convert both to lowercase strings

  if (val1.length !== val2.length) {
    return false;
  }

  word1 = val1.toLowerCase();
  word2 = val2.toLowerCase();

  //add values to object that counts the number of occurences

  w1Obj = {};
  w2Obj = {};

  for (const char of word1) {
    w1Obj[char] = (w1Obj[char] || 0) + 1;
  }

  for (const char of word2) {
    //Following if statement checks if the value of the char in object is not zero.
    //If its zero and the loop is still looking for a value, it will exit it.
    if (!w1Obj[char]) {
      return false;
    }
    w1Obj[char] -= 1;
  }

  return true;
}

console.log(
  isAnagram("mom", "mmz") ? "This is an Anagram" : "No its not an Anagram"
);
