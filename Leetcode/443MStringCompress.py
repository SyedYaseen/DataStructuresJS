def compress(chars):
    """
        :type chars: List[str]
        :rtype: int
        """
    current = ""
    currentCount = 0
    res = []

    for i in chars:
        if i == current:
            currentCount += 1
        else:
            current = i
            currentCount = 1

            if current != "":
                res.append(current)
                res.append(currentCount)

    return res


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
# "a2b2c3"
