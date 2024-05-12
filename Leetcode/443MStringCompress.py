def compress(chars):
    def appendCount(count):
        if count == 1:
            return []
        elif count > 9:
            return list(str(count))
        else:
            return [str(count)]
    current = ""
    currentCount = 0
    res = []
    if len(chars) == 1:
        return len(chars)

    for i in range(0, len(chars)):
        if i == 0:
            current = chars[i]
            currentCount = 1

        elif current == chars[i]:
            currentCount += 1

        elif current != chars[i]:
            res.append(current)
            res = res + appendCount(currentCount)
            current = chars[i]
            currentCount = 1

    res.append(current)
    res = res + appendCount(currentCount)

    for i in range(len(res)):
        chars[i] = res[i]
    return len(res)


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
print(compress(["a", "b", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b"]))
print(compress(["a", "b", "c"]))
