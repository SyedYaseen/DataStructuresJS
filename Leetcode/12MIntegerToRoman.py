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


numToRom = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
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
        print("Outerloop", current_num)
        while current_num > 0:

            if current_num == 9:
                result = result + numToRom[current_num*place]
                current_num -= 9
            elif current_num >= 5:
                result = result + numToRom[5*place]
                current_num -= 5
            elif current_num == 4:
                result = result + numToRom[4*place]
                current_num -= 4
            else:
                result += numToRom[place]
                current_num -= 1

        place /= 10
        index += 1

    return result


print(intToRoman(40))
