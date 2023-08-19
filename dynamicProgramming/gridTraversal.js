const gridTraversal = (row, col, memo = {}) => {
  if (row === 0 || col === 0) return 0;
  if (row === 1 && col === 1) return 1;

  let rcKey = `${row},${col}`;
  let rcKeyReverse = `${col},${row}`;

  if (rcKey in memo) return memo[rcKey];
  if (rcKeyReverse in memo) return memo[rcKeyReverse];

  memo[rcKey] =
    gridTraversal(row - 1, col, memo) + gridTraversal(row, col - 1, memo);

  return memo[rcKey];
};

// console.log(gridTraversal(2, 3));
// console.log(gridTraversal(5, 5));
// console.log(gridTraversal(3, 3));
// console.log(gridTraversal(18, 18));

const gridTraversalTab = (row, col) => {
  let table = new Array(row + 1).fill().map((r) => new Array(col + 1).fill(0));
  table[1][1] = 1;

  for (let i = 0; i <= row; i++) {
    for (let j = 0; j <= col; j++) {
      if (i + 1 <= row) table[i + 1][j] += table[i][j];
      if (j + 1 <= col) table[i][j + 1] += table[i][j];
    }
  }

  return table[row][col];
};

console.log(gridTraversalTab(3, 3));
