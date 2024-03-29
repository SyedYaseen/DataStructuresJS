# def twoSum(target, nums):
#     memo = {}

#     for i in nums:
#         complement = target - i
#         if complement in memo:
#             return [complement, i]
#         memo[i] = complement


# def threeSum(nums):
#     res = set()
#     for i in nums:
#         cop = nums[:]
#         cop.remove(i)
#         twoNums = twoSum(-i, cop)
#         if twoNums is not None:
#             twoNums.append(i)
#             twoNums.sort()
#             res.add(tuple(twoNums))
#     return list(res)


# # print(twoSum(8, [2, 3, 5]))
# nums = [-1, 0, 1, 2, -1, -4]
# # nums.remove(-1)
# # print(nums)
# print(threeSum(nums))


# def threeSum(nums):
#     memo = {}
#     result = set()
#     nums.sort()

#     for i in nums:
#         if i in memo:
#             result.add([i, memo[i]])
#             continue
#         copy = nums[:]
#         copy.remove(i)

#         twoSumMemo = {}
#         twoSumResult = set()

#         for j in copy:
#             complement = -i - j
#             if complement in twoSumMemo:
#                 twoSumResult.add(tuple([complement, j]))
#             twoSumMemo[complement] = complement
#             print(-i, j,    twoSumResult)


# nums = [-1, 0, 1, 2, -1, -4]
# print("Result", threeSum(nums))

def threeSum(nums):
    result = []
    nums.sort()

    for firstNum in nums:
        res = twoSum(nums, -firstNum)
        if res != None:
            res.append(firstNum)
        result.append(res)
    return res


def twoSum(numbers, target):
    res = None
    l, r = 0, len(numbers) - 1
    while l >= 0 and r < len(numbers) and l < r:
        sum = numbers[l] + numbers[r]
        print(sum)
        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l += 1
        elif sum > target:
            r -= 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print("Result", threeSum(nums))
