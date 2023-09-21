# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

import math


hash = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    50: "L",
    90: "XC",
    100: "C",
    500: "D",
    1000: "M"
}


def intToRoman(num: int) -> str:
    if num < 1 or num > 3999:
        return ""

    st = str(num)
    result = ""

    place = 10 ** (len(st) - 1)
    index = 0

    while index < len(st):
        current_num = int(st[index])

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

        while current_num > 0:
            value = current_num * place
            print("Place:", place, "value:", value)

            if current_num >= 5:
                result += result + hash[5*place]
                current_num -= current_num
            elif current_num == 4 or current_num == 9:
                result += result + hash[value]
                current_num -= current_num
            else:
                result += hash[place]
                current_num -= 1

        # result = hash[current_num] + result

        place /= 10
        index += 1

    # if digits == 1:
    #     for i in range(num):
    #         result = result + "I"

    return result


print(intToRoman(88))
