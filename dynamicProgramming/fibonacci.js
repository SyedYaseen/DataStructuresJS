const fib = (n, memo = {}) => {
  while (n <= 2) return 1;
  if (n in memo) return memo[n];
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
  return memo[n];
};

// console.log(fib(50));
// 12586269025;

// Tabulation fib
const fibTab = (n) => {
  let table = new Array(n + 1).fill(0);
  table[0] = 0;
  table[1] = 1;

  for (let i = 0; i < table.length; i++) {
    if (i + 1 <= n) table[i + 1] += table[i];
    if (i + 2 <= n) table[i + 2] += table[i];
  }
  return table;
};

console.log(fibTab(50));
