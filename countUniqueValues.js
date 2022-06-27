//solution 1

// function countUniqueValues(sortedArr) {
//   left = 0;
//   right = sortedArr.length - 1;
//   uniqueCounter = 0;

//   while (left < right) {
//     sortedArr[left] === sortedArr[left + 1]
//       ? left++
//       : (uniqueCounter++, left++);
//     sortedArr[right] === sortedArr[right - 1]
//       ? right--
//       : (uniqueCounter++, right--);
//   }
//   return uniqueCounter;
// }

// console.log(countUniqueValues([1, 2, 2, 3, 5, 7, 7, 8]));

//solution 2

function countUniqueValues(sortedArr) {
  let i = 0;
  let j = 1;

  for (let j = 0; j < sortedArr.length; j++) {
    if (i !== j) {
      i++;
      sortedArr[i] = sortedArr[j];
    }
  }
  return i;
}

console.log(countUniqueValues([1, 2, 2, 3, 5]));
