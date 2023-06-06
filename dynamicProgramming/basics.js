const dib = (n) => {
  if (n <= 1) {
    console.log(n);
    return;
  }
  console.log(n);
  dib(n - 1);
  console.log("Done");
  dib(n - 1);
};

dib(5);