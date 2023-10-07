import math


class Solution(object):

    def func(self, nums, target):
        low, high = 0, len(nums) - 1
        pos1 = None
        pos2 = None

        while low <= high:
            mid = (low + high) // 2
            print(mid)

            if nums[mid] == target:
                pos1 = pos2 = mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        print(pos1, pos2)

        if pos1 is not None:
            while pos1 >= 0 and nums[pos1] == target:
                pos1 -= 1
            while pos2 < len(nums) and nums[pos2] == target:
                pos2 += 1
            return [pos1 + 1, pos2 - 1]
        else:

            return [-1, -1]


sln = Solution()
# print(sln.func([5, 7, 7, 8, 8, 10], 8))
print(sln.func([1], 1))
# print(sln.func([1], 1))
