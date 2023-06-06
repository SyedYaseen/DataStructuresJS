/*
canSum(7, [4, 2])
Can the target sum be created from values in array
Values in array can be used multiple times

Pseudo:
Start at 7 on tree
There will n options where n is # values in arr
Each option will have n options
Base case:
  1. value of node = 0 
  2. value of options is >= 0

*/

const canSum = (target, arr, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === 0) return true;
  if (target < 0) return false;

  for (const num of arr) {
    let result = canSum(target - num, arr, memo);
    memo[target] = result;
    if (result === true) return true;
  }

  return false;
};

// console.log(canSum(7, [5, 3, 4, 7]));
// console.log(canSum(8, [2, 3, 5]));
// console.log(canSum(300, [7, 14, 10]));

/*
howSum(7, [4, 2])
Can the target sum be created from values in array
return the array that would create the values
Values in array can be used multiple times
If not present return null

*/

const howSum = (target, arr) => {
  if (target === 0) return [];
  if (target < 0) return null;

  for (const num of arr) {
    let result = howSum(target - num, arr);

    if (result !== null && result.length > 0) {
      return [num, ...result];
    }
  }

  return null;
};

// console.log(howSum(6, [2]));
// console.log(howSum(7, [5, 3, 4]));
// console.log(howSum(8, [2, 3, 5]));
// console.log(howSum(300, [7, 14]));
let memo = {};

const howSumMemo = (target, arr) => {
  if (target in memo) return memo[target];
  if (target === 0) return [];
  if (target < 0) return null;

  let result;
  for (const num of arr) {
    result = howSumMemo(target - num, arr, memo);

    if (result !== null) {
      memo[target] = [num, ...result];
      return memo[target];
    }
  }

  memo[target] = null;
  return null;
};

// console.log(howSumMemo(6, [5, 2, 3]));
// console.log(howSumMemo(7, [5, 3, 4, 7]));
// console.log(howSumMemo(8, [2, 3, 5]));
// console.log(howSumMemo(300, [5, 15, 30, 10]));
// console.log(memo);

const bestSum = (target, arr) => {
  if (target === 0) return [];
  if (target < 0) return null;

  let resultArr = null;

  for (const num of arr) {
    let result = bestSum(target - num, arr);

    if (
      result !== null &&
      (resultArr === null || result.length < resultArr.length)
    )
      resultArr = [num, ...result];
  }

  return resultArr;
};

// console.log(bestSum(6, [5, 2, 3]));
// console.log(bestSum(7, [5, 3, 4, 7]));
// console.log(bestSum(8, [2, 3, 5]));
// console.log(bestSum(300, [5, 15, 30, 10]));
// console.log(memo);

const bestSumMemo = (target, arr, memo = {}) => {
  if (target === 0) return [];
  if (target < 0) return null;
  if (target in memo) return memo[target];

  let resultArr = null;

  for (const num of arr) {
    let result = bestSumMemo(target - num, arr, memo);

    if (
      result !== null &&
      (resultArr === null || result.length < resultArr.length)
    ) {
      resultArr = [num, ...result];
    }
  }
  memo[target] = resultArr;
  return resultArr;
};

// console.log(bestSumMemo(6, [5, 2, 3]));
// console.log(bestSumMemo(7, [5, 3, 4, 7]));
// console.log(bestSumMemo(8, [2, 3, 5]));
console.log(bestSumMemo(300, [5, 15, 30, 10]));
// console.log(memo);
