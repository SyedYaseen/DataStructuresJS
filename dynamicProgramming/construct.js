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
//     ["ee", "eee", "eeeee", "eeeee", "eeeeeee", "f"]
//   )
// );
// console.log(countComboMemo("purple", ["purp", "p", "ur", "le", "purpl"]));

const allConstruct = (target, wordBank) => {
  if (target === "") return [];

  // let allCombo = null;
  let combo = null;
  for (const word of wordBank) {
    if (target.includes(word)) {
      let slicedTarget = target.replace(word, "");
      let result = allConstruct(slicedTarget, wordBank);

      if (result !== null && result.length >= 0) {
        if (combo === null) combo = [...result, word];
        else combo.push([...result, word]);
      }
    }
  }

  if (combo === null) return null;
  return [combo];
};

// console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
