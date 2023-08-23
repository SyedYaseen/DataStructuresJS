let findMedianSortedArrays = function (nums1, nums2) {
  const l1 = nums1.length
  const l2 = nums2.length

  let sum = l1 + l2
  let odd = sum % 2 !== 0 ? true : false
  let medianIndex = null

  let m1 = null
  let m2 = null

  if (odd) {
    medianIndex = Math.floor(sum / 2)
  } else {
    medianIndex = sum / 2
  }

  let i = 0
  let j = 0

  let count = i + j

  while (count <= medianIndex) {
    if (count === medianIndex) {
    }

    if (i === l1) {
      j = j + medianIndex - count
      if (m1 === null && !odd) m1 = nums2[j - 1]
      m2 = nums2[j]
    }

    if (j === l2) {
      i = i + medianIndex - count

      if (m1 === null && !odd) m1 = nums1[i - 1]
      m2 = nums1[i]
    }

    if (nums1[i] < nums2[j]) {
      if (count === medianIndex - 1 && !odd) m1 = nums1[i]
      if (count === medianIndex) m2 = nums1[i]
      i++
    } else {
      if (count === medianIndex - 1 && !odd) m1 = nums2[j]
      if (count === medianIndex) m2 = nums2[j]
      j++
    }

    count = i + j
  }
  return odd ? m2 : (m1 + m2) / 2
}

nums1 = [1, 2]
nums2 = [3, 4]

console.log(findMedianSortedArrays(nums1, nums2))

//Backup with creating a sorted array until median
// let findMedianSortedArrays = function (nums1, nums2) {
//   const l1 = nums1.length
//   const l2 = nums2.length

//   let sum = l1 + l2
//   let odd = sum % 2 !== 0 ? true : false
//   let medianIndex = 0

//   let result = []

//   let m1 = 0
//   let m2 = 0

//   if (odd) {
//     medianIndex = Math.floor(sum / 2)
//   } else {
//     medianIndex = sum / 2 //choose this and value below it
//   }

//   let  i = 0
//   let  j = 0

//   let count = 0

//   while (count <= medianIndex) {
//     if (count === medianIndex) {
//     }

//     if ( i === l1) {
//       // nums2 = nums2.slice( j)
//       // return [...result, ...nums2]
//     }

//     if ( j === l2) {
//       // nums1 = nums1.slice( i)
//       // return [result, nums1]
//     }

//     if (nums1[ i] < nums2[ j]) {
//       result.push(nums1[ i])

//       if (count === medianIndex - 1 && !odd) {
//         m1 = nums1[ i]
//       }

//       if (count === medianIndex && !odd) {
//         m2 = nums1[ i]
//       }

//       if (count === medianIndex && odd) {
//         m2 = nums1[ i]
//       }

//        i++
//     } else {
//       result.push(nums2[ j])
//       if (count === medianIndex - 1 && !odd) {
//         m1 = nums2[ j]
//       }

//       if (count === medianIndex && !odd) {
//         m2 = nums2[ j]
//       }

//       if (count === medianIndex && odd) {
//         m2 = nums2[ j]
//       }
//        j++
//     }

//     count++
//   }
//   console.log(m1, m2)
//   return result, odd ? m2 : (m1 + m2) / 2
// }

// nums1 = [10, 30]
// nums2 = [20, 50]

// console.log(findMedianSortedArrays(nums1, nums2))
