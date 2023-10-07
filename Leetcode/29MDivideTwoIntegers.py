def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    def checkBounds(number):
        if number > (2**31) - 1:
            return 2**31 - 1
        if number < -2**31:
            return -2**31
        return None

    def checkSign(dividend, divisor):
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return -1
        else:
            return 1

    if dividend == 0:
        return 0

    flag = checkSign(dividend, divisor)
    if abs(divisor) == 1:
        bounds = checkBounds(-flag * dividend)
        if bounds is not None:
            return bounds
        else:
            return flag * dividend

    res = 0

    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)

    while dividend_abs >= 0:
        dividend_abs = dividend_abs - divisor_abs
        res += 1

    if dividend_abs != 0:
        res -= 1

    bounds = checkBounds(flag * res)
    if bounds is not None:
        return bounds
    else:
        return -flag * res


# print(divide(-10, -5))
# print(divide(-2147483648, -1))
print(divide(-1, 1))

print("expected", - 1)
