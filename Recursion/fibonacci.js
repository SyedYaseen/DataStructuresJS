function findFib(num) {
  let fib = [1, 1];

  function fibonacci() {
    let fibLen = fib.length;

    if (fibLen === num) return;
    fib.push(fib[fibLen - 1] + fib[fibLen - 2]);

    fibonacci();
  }

  fibonacci();
  return fib[num - 1];
}

console.log(findFib(35));

// initialize first two numbers
// find last two numbers
// keep adding last two numbers until fib length = num length
// return last value in fib

// actual solution
function fib(n) {
  if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
}
