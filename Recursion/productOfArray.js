function productOfArray(arr) {
  if (arr.length === 0) return 1;
  return arr.pop() * productOfArray(arr);
}

console.log(productOfArray([1, 5, 20]));
