def romanToInt(s):
    romToNum = {
        "I":  1,
        "IV": 4,
        "V":  5,
        "IX": 9,
        "X":  10,
        "XL": 40,
        "L":  50,
        "XC": 90,
        "C":  100,
        "CD": 400,
        "D":  500,
        "CM": 900,
        "M":  1000
    }

    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            nextTwoChar = s[i] + s[i+1]
            if nextTwoChar in romToNum:
                result += romToNum[nextTwoChar]
                i += 2
                continue

        result += romToNum[s[i]]
        i += 1

    return result


print(romanToInt('MCMXCIV'))
