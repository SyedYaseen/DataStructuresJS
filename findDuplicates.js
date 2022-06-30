function containsDuplicates(arr) {
  obj = {};
  for (const char of arr) {
    if (obj[char]) return true;
    obj[char] = (obj[char] || 0) + 1;
  }
  return false;
}

console.log(containsDuplicates([1, 2, 3, 5]));
