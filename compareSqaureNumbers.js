const compare = (arr1, arr2) => {
  if (arr1.length !== arr2.length) {
    return false;
  }

  let numbers = {};
  let square = {};

  arr1.forEach((element) => {
    numbers[element] = (numbers[element] || 0) + 1;
  });

  arr2.forEach((element) => {
    square[element] = (square[element] || 0) + 1;
  });

  console.log(numbers, square);

  for (const key in numbers) {
    if (square[key ** 2] !== numbers[key]) {
      return false;
    }

    if (!(key ** 2 in square)) {
      return false;
    }
  }
  return true;
};

console.log(compare([1, 1, 2, 3], [1, 1, 4, 9]));
