def BuySell(nums):
    i = 0
    j = 0
    currentProfit = -99999999999999999

    while i <= j and j < len(nums):
        diff = nums[j] - nums[i]

        if nums[i] > nums[j]:
            i += 1
            continue

        elif diff > currentProfit:
            currentProfit = diff

        j += 1

    return currentProfit


print(BuySell([7, 1, 5, 3, 6, 4]))
