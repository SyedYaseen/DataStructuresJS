class Solution(object):
    def func(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = None
        l, r = 0, len(numbers) - 1
        while l >= 0 and r < len(numbers) and l < r:
            sum = numbers[l] + numbers[r]
            print(sum)
            if sum == target:
                return l + 1, r + 1
            elif sum < target:
                l += 1
            elif sum > target:
                r -= 1

        return res


sln = Solution()
print(sln.func([2, 7, 11, 15], 9))
