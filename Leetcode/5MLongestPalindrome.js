// Example 1:
// Input: s = "babad"
// Output: "bab"
// Explanation: "aba" is also a valid answer.

// Example 2:
// Input: s = "cbbd"
// Output: "bb"

const longestPalindrome = (s) => {
  let substr = ""
  let longest = ""
  let len = s.length

  if (len === 1) return s
  if (len === 0) return ""

  for (let i = 0; i < s.length; i++) {
    substr = s.substr(0, i + 1)
    let i,
      j = checkPalindrome(substr)
    if (checkPalindrome(substr)) {
      if (longest.length < substr.length) longest = substr
    }
  }

  return longest
}

const checkPalindrome = (s) => {
  // if (s === "") return false
  len = s.length
  // if (len === 1) return true

  let mid = Math.floor(len / 2)

  i = 0
  j = 0

  if (len % 2 !== 0) {
    i = mid
    j = i
  } else {
    i = mid - 1
    j = i + 1
  }
  while (i >= 0 && j < len && s[i] === s[j]) {
    i--
    j++
  }

  return i, j
}

// str = ["babad", "cbbd", "ac", "abahsain", "mom", "1331"]

str = ["cbbd"]
str.forEach((s) => console.log(longestPalindrome(s)))
