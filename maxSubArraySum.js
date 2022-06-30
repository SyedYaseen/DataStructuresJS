function maxSubArraySum(arr, num) {
  let tempSum = 0;
  let maxSum = 0;

  for (let i = 0; i < num; i++) {
    tempSum += arr[i];
  }
  maxSum = tempSum;

  for (let i = 1; i < arr.length - num + 1; i++) {
    tempSum = tempSum - arr[i - 1] + arr[i + num - 1];
    if (tempSum > maxSum) {
      maxSum = tempSum;
    }
  }

  return maxSum;
}

console.log(maxSubArraySum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4));
// console.log(maxSubArraySum([100, 200, 300, 400], 2));
