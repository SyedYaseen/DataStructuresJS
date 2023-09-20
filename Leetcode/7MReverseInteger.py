def reverse(number):
    temp = str(number)
    res = 0

    if temp[0] == "-":
        res = int(temp[:0:-1]) * -1
    else:
        res = int(temp[::-1])

    if res >= (2 ** 31) - 1 or res <= -2 ** 31:
        res = 0
    return res


print(reverse(1534236469))
