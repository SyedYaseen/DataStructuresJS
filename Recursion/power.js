function power(base, pow) {
  if (pow === 0) return 1;
  if (pow === 1) return base;
  //   pow--;
  return base * power(base, --pow);
}

console.log(power(5, 0));
