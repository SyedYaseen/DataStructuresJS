//  Input: s = "PAYPALISHIRING", numRows = 4
//  Output: "PINALSIGYAHRPI"
//  Explanation:
//  0123 4567 8901 23
//  PAYP ALIS HIRI NG

//  P    I    N    5
//  A  L S  I G  4 7
//  Y A  H R  1 3  8
//  P    I    2    9
//  Top and bottom rows need "numRows" spaces between each

// 0   4   8
// 1 3 5 7 9
// 2   6   10

// Add a 2D array
// two for loops
// oscillator - goes to 0 - n and n to 0 - y axis
// when it goes back up - move x
// Else dont move x

//  P     H
//  A   S I
//  Y  I  R
//  P L   I G
//  A     N

// 14 char
// rows 3
//  P   A   H   N
//  A P L S I I G
//  Y   I   R

const convert = (s, numRows) => {
  if (numRows === 1) return s

  let l = s.length

  if (l <= numRows) return s

  let result = new Array(numRows)
    .fill("")
    .map(() => new Array(s.length).fill(""))

  let x = 0
  let y = 0
  let decrement = false

  for (let i = 0; i < s.length; i++) {
    result[y][x] = s[i]

    if (y === numRows - 1) decrement = true
    if (y === 0) decrement = false

    if (decrement) {
      x += 2
      y -= 1
    } else {
      y += 1
    }
  }

  let st = ""
  for (let i = 0; i < result.length; i++) {
    for (let j = 0; j < result[i].length; j++) {
      let c = result[i][j]
      if (c !== undefined) st += result[i][j]
    }
  }
  return st
}

// console.log(convert("PAYPALISHIRING", 3))
console.log(convert("GREEE", 3))
