# 14 char
# rows 3
#  P   A   H   N
#  A P L S I I G
#  Y   I   R

def convert(s, numRows):
    if numRows == 1 or len(s) <= numRows:
        return s

    cols = len(s)
    arr = [["" for i in range(cols)] for j in range(numRows)]

    x = 0
    y = 0
    decrement = False

    for i in s:
        arr[y][x] = i
        if (y == numRows - 1):
            decrement = True
        if (y == 0):
            decrement = False

        if (decrement):
            x += 2
            y -= 1
        else:
            y += 1

    str = ""

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            str += arr[i][j]

    return str


# convert("PAYPALISHIRING", 3)
print(convert("SAU", 3))
