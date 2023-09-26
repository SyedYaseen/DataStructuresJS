numToLetters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letterCombinations(digits):
    if digits == "":
        return []
    base = numToLetters[digits[0]]
    return populate(digits[1:], base)

def populate(digit, base):
    if len(digit) == 0:
        return base
    current = numToLetters[digit[0]]
    temp = []
    for i in base:
        for j in current:
            temp.append(i+j)

    return populate(digit[1:], temp)


letterCombinations("27")
