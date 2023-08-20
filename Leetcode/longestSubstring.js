// Example 1:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// const sub = (s) => {
//   let mapStr = {}
//   let size = 0
//   let longest = 0

//   for (let i = 0; i < s.length; i++) {
//     if (s[i] in mapStr) {
//       if (size > longest) longest = size
//       mapStr = {}
//       size = 0
//     }
//     mapStr[s[i]] = 1
//     size += 1

//     console.log("Size here", s[i], size)
//   }

//   if (size > longest) longest = size
//   return longest
// }

// j - i <= longest

// let s = ["pwwkew", "abcabcbb", "dvdf"]

// const sub = (str) => {
//   let i = 0
//   let j = 0
//   let longest = 0

//   while (i <= j && j < str.length) {
//     if (str[i] != str[j]) {
//       if (longest < i - j + 1 || longest === 0) longest = j - i + 1
//     }
//     if (str[i] === str[j] && i !== j) i = i + 1
//     j += 1
//     console.log("longest", longest, "i", i, str[i], "j", j, str[j])
//   }
//   return longest
// }

// s.forEach((str) => console.log(sub(str)))

// let s = ["pwwkew", "abcabcbb", "dvdf"]
let s = ["abcabcbb"]

const sub = (str) => {
  let i = 0
  let j = 0
  let longest = 0
  let current = 0
  let len = str.length
  let hash = {}

  if (len === 0) return 0
  if (len === 1) return 1

  if (len === 2 && str[0] === str[1]) return 1
  if (len === 2 && str[0] !== str[1]) return 2

  while (j < len) {
    if (i === j) {
      hash[str[j]] = 1
      current = j - i + 1
    }

    if (s[j] in hash && i !== j) {
      delete hash[str[j]]
      current = j - i + 1
      if (longest < current) longest = current
      i += 1
      j = i
      continue
    }

    if (str[i] !== str[j]) {
      hash[str[j]] = 1
      current = j - i + 1
    }

    j += 1
  }

  return longest
}

s.forEach((str) => console.log(sub(str)))
// console.log("longest", longest, "   ", "i:", i, str[i], "   ", "j:", j, str[j])

// while (j < str.length) {
//   if (i === j) {
//     hash[str[j]] = 1
//     j += 1
//   }

//   if (str[j] in hash) {
//     if (longest < current) longest = current
//     delete hash[str[j]]
//     i += 1
//     j = i
//     current = 0
//     continue
//   }

//   if (str[i] !== str[j]) {
//     current = j - i + 1
//     hash[str[j]] = 1
//   }
//   j += 1
// }
