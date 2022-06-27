//Find consecutive sum

function consSum(arr, num) {
  let tempSum = 0;
  let maxSum = 0;
  for (let i = 0; i < num; i++) {
    tempSum += arr[i];
    console.log("initial sum", tempSum);
  }
  maxSum = tempSum;

  for (let i = 1; i < arr.length - num + 1; i++) {
    tempSum = tempSum - arr[i - 1] + arr[i + num - 1];
    // console.log("sum is", tempSum, "sub", arr[i - 1], "add", arr[i + num - 1]);
    tempSum > maxSum ? (maxSum = tempSum) : null;
  }
  return maxSum;
}

console.log(consSum([4, 5, 3, 2, 13, 4, 5, 19], 4));
