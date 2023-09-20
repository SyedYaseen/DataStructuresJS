# def isPalindrome(x: int) -> bool:
#     st = str(x)
#     i = 0
#     j = len(st) - 1

#     while j >= i:
#         print(st[i], st[j])
#         if (st[i] != st[j]):
#             return False
#         i += 1
#         j -= 1

#     return True

# The fastest solution is:


def isPalindrome(x: int) -> bool:
    soln = str(x)
    return soln == soln[::-1]


print(isPalindrome(1000021))
