import math


class Solution(object):
    def func(self, numbers, target):

        low, high = 0, len(numbers) - 1

        while low <= high:
            mid = (low + high) // 2

            if numbers[mid] == target:
                return mid

            if numbers[low] <= numbers[mid]:
                if numbers[low] <= target < numbers[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if numbers[mid] < target <= numbers[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def func2(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        while (numbers[low] >= numbers[high]):
            if numbers[low] == target:
                return low
            if numbers[high] == target:
                return high
            low += 1
            high -= 1

        return -1


sln = Solution()
print(sln.func([4, 5, 6, 7, 0, 1, 2, 3], 0))
# print(sln.func([1], 1))
