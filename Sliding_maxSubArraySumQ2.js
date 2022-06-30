function maxSubArraySum(arr, num) {
  let tempArrSize = 0;
  let minArrSize = 0;
  let sum = 0;

  while (sum < num) {
    sum += arr[tempArrSize];
    tempArrSize++;
  }
  minArrSize = tempArrSize;

  for (let i = 1; i < arr.length - num + 1; i++) {
    tempSum = tempSum - arr[i - 1] + arr[i + num - 1];
    if (tempSum > maxSum) {
      maxSum = tempSum;
    }
  }

  return minArrSize;
}

console.log(maxSubArraySum([2, 3, 1, 2, 4, 3], 7));
// console.log(maxSubArraySum([100, 200, 300, 400], 2));
