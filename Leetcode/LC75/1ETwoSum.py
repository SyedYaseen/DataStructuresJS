# def twoSum(nums, target):
#     complementSet = {}
#     for i in range(0, len(nums)):
#         complement = target - nums[i]

#         if nums[i] in complementSet:
#             return [complementSet[nums[i]], i]
#         complementSet[complement] = i


def twoSum(nums, target):
    complementSet = {}
    for i in range(0, len(nums)):
        complement = target - nums[i]

        if complement in complementSet:
            return [complementSet[complement], i]
        complementSet[nums[i]] = i


print(twoSum([2, 1, 5, 3], 4))
print(twoSum([2, 7, 11, 15], 9))
