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
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def intToRoman(num: int) -> str:
    if num < 1 or num > 3999:
        return ""

    st = str(num)
    digits = len(st)
    result = ""

    place = 1
    for i in st:

        print(i)
    # if digits == 1:
    #     for i in range(num):
    #         result = result + "I"

    return result


print(intToRoman(3))
