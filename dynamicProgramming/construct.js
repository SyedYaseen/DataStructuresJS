const canConstruct = (target, wordBank) => {
  if (target === "") return true;

  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      result = canConstruct(slicedTarget, wordBank);

      if (result === true) return result;
    }
  }
  return false;
};

// With memo
const canConstructMemo = (target, wordBank, memo = {}) => {
  if (target === "") return true;
  if (target in memo) return memo[target];

  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      result = canConstructMemo(slicedTarget, wordBank, memo);
      memo[target] = result;
      if (result === true) return result;
    }
  }
  return false;
};

// console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcdef"]));
// console.log(
//   canConstructMemo(
//     "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff",
//     ["ee", "eee", "eeeee", "eeeee", "eeeeeee"]
//   )
// );

const howConstruct = (target, wordBank) => {
  if (target === "") return [];

  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = howConstruct(slicedTarget, wordBank);

      if (result !== null && result.length >= 0) return [...result, word];
    }
  }
  return null;
};

const howConstructMemo = (target, wordBank, memo = {}) => {
  if (target === "") return [];
  if (target in memo) return memo[target];

  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = howConstructMemo(slicedTarget, wordBank, memo);

      if (result !== null && result.length >= 0) {
        memo[target] = [...result, word];
        return memo[target];
      }
    }
  }
  memo[target] = null;
  return null;
};

// console.log(howConstruct("abcdef", ["ab", "abc", "cd", "def", "abcdef"]));
// console.log(
//   howConstructMemo(
//     "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff",
//     ["ee", "eee", "eeeee", "eeeee", "eeeeeee", "f"]
//   )
// );

const bestConstruct = (target, wordBank) => {
  if (target === "") return [];

  let bestCombo = null;
  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = bestConstruct(slicedTarget, wordBank);

      if (
        result !== null &&
        result.length >= 0 &&
        (bestCombo === null || result.length < bestCombo.length)
      ) {
        bestCombo = [...result, word];
      }
    }
  }
  return bestCombo;
};

// Incomplete
const bestConstructMemo = (target, wordBank, memo = {}) => {
  if (target === "") return [];
  if (target in memo) return memo[target];
  let bestCombo = null;

  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = bestConstruct(slicedTarget, wordBank, memo);

      if (
        result !== null &&
        result.length >= 0 &&
        (bestCombo === null || result.length < bestCombo.length)
      ) {
        bestCombo = [...result, word];
      }
    }
  }

  memo[target] = bestCombo;
  return bestCombo;
};

// console.log(
//   bestConstructMemo(
//     "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff",
//     ["ee", "eee", "eeeee", "eeeee", "eeeeeee", "f"]
//   )
// );

// console.log(bestConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcdef"]));
// console.log(bestConstruct("abcdef", ["ab", "abc", "cd", "def", "abcdef"]));

//Here I am check if the word is present anywhere at all

const countCombo = (target, wordBank) => {
  if (target === "") return 1;

  let count = 0;
  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      count = count + countCombo(slicedTarget, wordBank);
    }
  }

  return count;
};

//Here I am checking if the word is present only as a prefix. Hence using slice

const countComboSlice = (target, wordBank) => {
  if (target === "") return 1;

  let count = 0;
  for (const word of wordBank) {
    if (target.indexOf(word) === 0) {
      const numWays = countComboSlice(target.slice(word.length), wordBank);

      count = count + numWays;
    }
  }

  return count;
};

// console.log(countComboSlice("purple", ["purp", "p", "ur", "le", "purpl"]));
// console.log(countCombo("abcdef", ["ab", "abc", "cd", "def", "abcdef"]));

const countComboMemo = (target, wordBank, memo = {}) => {
  if (target === "") return 1;
  if (target in memo) return memo[target];

  let count = 0;
  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      count = count + countComboMemo(slicedTarget, wordBank, memo);
    }
  }
  memo[target] = count;
  return count;
};

// console.log(countComboMemo("abcdef", ["ab", "abc", "cd", "def", "abcdef"]));
// console.log(
//   countComboMemo(
//     "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff",
//     ["ee", "eee", "eeeee", "eeeee", "eeeeeee"]
//   )
// );
// console.log(countComboMemo("purple", ["purp", "p", "ur", "le", "purpl"]));

const allConstruct = (target, wordBank) => {
  if (target === "") return [[]];

  let combo = [];
  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = allConstruct(slicedTarget, wordBank);

      if (result.length !== 0)
        combo = combo.concat(result.map((innerCombo) => [...innerCombo, word]));
    }
  }

  if (combo === null) return [];
  return combo;
};

// let res = allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]);
// console.log(res);
// console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));

const allConstructMemo = (target, wordBank, memo = {}) => {
  if (target === "") return [[]];
  if (target in memo) return memo[target];

  let combo = [];
  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = allConstructMemo(slicedTarget, wordBank);

      if (result.length !== 0)
        combo = combo.concat(result.map((innerCombo) => [...innerCombo, word]));
    }
  }

  memo[target] = combo;
  return combo;
};

/* 
In this problem the best case is a exponential memory, because it needs to go through the 
all the combos on the leaf. So it wont return a value even its memoized. It throws a 
out of memory error.
*/

const allConstructMemoSlice = (target, wordBank, memo = {}) => {
  if (target === "") return [[]];
  if (target in memo) return memo[target];

  let combo = [];
  for (const word of wordBank) {
    if (target.indexOf(word) === 0) {
      let suffix = target.slice(word.length);
      let suffixWays = allConstructMemoSlice(suffix, wordBank, memo);
      let targetWays = suffixWays.map((way) => [word, ...way]);
      combo = combo.concat(targetWays);
    }
  }

  memo[target] = combo;
  return combo;
};

// let res = allConstructMemoSlice("abcdef", [
//   "ab",
//   "abc",
//   "cd",
//   "def",
//   "abcd",
//   "ef",
//   "c",
// ]);
// console.log(res);

console.log(
  allConstructMemoSlice(
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff",
    ["ee", "eee", "eeeee", "eeeee", "eeeeeee", "ff"]
  )
);

// console.log(
//   allConstructMemoSlice("purple", ["purp", "p", "ur", "le", "purpl"])
// );

// let a = [
//   ["dfsdfa", "b", "c"],
//   ["d", "e"],
// ];
// let b = [["g", "h"]];
// let d = [];
// d = a.map((x) => [...x, "val"]);
// console.log(d);
// console.log([...a, ...b]); // [ [ 'dfsdfa', 'b', 'c' ], [ 'd', 'e' ], [], [ 'g', 'h' ] ]
