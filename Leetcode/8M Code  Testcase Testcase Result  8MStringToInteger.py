# Skipping because the requirements arent complete,
# too many potential edge cases

def myAtoi(s: str) -> int:
    s = s.strip()
    result = ""
    index = 0

    while index < len(s):
        print(s[index])
        index += 1


print(myAtoi("   432"))


# [-231, 231 - 1]
