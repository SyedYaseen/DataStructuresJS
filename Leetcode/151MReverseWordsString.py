def reverseWords(s):
    """
        :type s: str
        :rtype: str
        """
    return " ".join(s.split()[::-1])


reverseWords("the sky is blue")
reverseWords("  hello world  ")
