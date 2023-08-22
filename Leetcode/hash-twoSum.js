nums = [2, 7, 11, 15]
target = 9

// Brute force
let twoSumBf = function (nums, target) {
  for (i = 0; i < nums.length; i++) {
    for (j = 0; j < nums.length; j++) {
      if (nums[i] === nums[j]) break
      if (nums[i] + nums[j] === target) {
        return [i, j]
      }
    }
  }
}

// Hash table
let twoSumhash = (nums, target) => {
  let indexMap = {}
  for (let i = 0; i < nums.length; i++) {
    indexMap[nums[i]] = i
  }

  for (let i = 0; i < nums.length; i++) {
    complement = target - nums[i]
    if (complement < 0) break
    if (complement in indexMap && indexMap[complement] != i)
      return [indexMap[complement], i]
  }
}

// one iteration hash table
let twoSum = (nums, target) => {
  let indexMap = {}
  for (let i = 0; i < nums.length; i++) {
    complement = target - nums[i]
    if (complement in indexMap) return [indexMap[complement], i]
    indexMap[nums[i]] = i
  }
}

console.log(twoSum(nums, target))
