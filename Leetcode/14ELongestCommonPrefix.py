def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    largestIndex = len(strs[0]) - 1

    result = strs[0]
    for word in strs[1:]:
        if len(word) < len(result):
            largestIndex = len(word) - 1
            result = result[0:largestIndex + 1]

        for j in range(largestIndex):
            if result[j] != word[j]:
                largestIndex = j
                if largestIndex == 0:
                    return ""
                result = result[0:j]

    return result


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["ab", "a"]))


# Input: strs = ["flower","flow","flight"]
# Output: "fl"
