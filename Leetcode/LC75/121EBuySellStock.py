def BuySell(nums):
    i = 0
    j = 1
    currentProfit = -99999999999999999

    while i < j:
        diff = nums[j] - nums[i]
        if nums[i] - nums[j]:
            i += 1

        if diff > currentProfit:
            currentProfit = diff

        j += 1
    return currentProfit


print(BuySell([7, 1, 5, 3, 6, 4]))
