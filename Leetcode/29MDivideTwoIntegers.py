def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend

    res = 0

    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)

    while dividend_abs > 0:
        dividend_abs = dividend_abs - divisor_abs
        res += 1

    if dividend_abs != 0:
        res -= 1

    print("divi", dividend_abs)

    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        return -1 * res

    return res


print(divide(10, 3))
