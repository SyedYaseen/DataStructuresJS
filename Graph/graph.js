let graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

/* This looks like a queue */
function breadthFirst(graph, source) {
  let queue = [source];

  while (queue.length > 0) {
    let current = queue.shift();
    console.log(current);

    let neighbours = graph[current];
    neighbours.forEach((neighbour) => {
      queue.push(neighbour);
    });
  }
}

function depthFirst(graph, source) {
  let stack = [source];
  while (stack.length > 0) {
    let current = stack.pop();
    let neighbours = graph[current];
    console.log(current);

    neighbours.forEach((neighbour) => {
      stack.push(neighbour);
    });
  }
}

function depthFirstRecursion(graph, source) {
  let neighbours = graph[source];
  console.log(source);

  neighbours.forEach((neighbour) => {
    depthFirst(graph, neighbour);
  });
}

// breadthFirst(graph, "a")
// depthFirst(graph, 'a')
// depthFirstRecursion(graph, "a")

//////////////// Has path

graph = {
  f: ["g", "i"],
  g: ["h"],
  h: [],
  i: ["g", "k"],
  j: ["i"],
  k: [],
};

// Is there a path from f to k?

//Recursion not working
function hasPathDfRec(graph, source, dest) {
  if (source === dest) return true;

  for (let neighbour of graph[source]) {
    if (hasPathDfRec(graph, neighbour, dest) === true) return true;
  }

  //why is this not woring?
  // let neighbours = graph[source]
  // neighbours.forEach(neighbour => {
  //   if(hasPathDfRec(graph, neighbour, dest) === true) return true
  // })

  return false;
}

// console.log(hasPathDfRec(graph, "f", "k"))

// Soln using depth first
function hasPathDf(graph, source, destination) {
  let stack = [source];
  let hasPath = false;
  while (stack.length > 0) {
    let current = stack.pop();
    if (current === destination) hasPath = true;

    graph[current].forEach((neighbour) => stack.push(neighbour));
  }
  return hasPath;
}
// console.log(hasPathDf(graph, "k", "f"))

//Soln using breath first
function hasPathBf(graph, source, destination) {
  let queue = [source];
  let hasPath = false;
  while (queue.length > 0) {
    let current = queue.shift();
    if (current === destination) hasPath = true;

    graph[current].forEach((neighbour) => queue.push(neighbour));
  }
  return hasPath;
}
// console.log(hasPathBf(graph, "f", "k"))

let edgeList = [
  ["i", "j"],
  ["k", "i"],
  ["m", "k"],
  ["k", "l"],
  ["o", "n"],
];

graph = {};
function EgdeListToGraph(edgeList) {
  for (const entry of edgeList) {
    let [source, destination] = entry;
    if (!(source in graph)) {
      graph[source] = [];
    }

    if (!(destination in graph)) {
      graph[destination] = [];
    }

    graph[source].push(destination);
    graph[destination].push(source);
  }
}

EgdeListToGraph(edgeList);

function checkPath(src, dest) {
  console.log(hasPath(src, dest, graph, new Set()));
}

function hasPath(src, dest, graph, visited) {
  if (src === dest) return true;
  if (visited.has(src)) return false;

  visited.add(src);

  for (let neigh of graph[src]) {
    if (hasPath(neigh, dest, graph, visited) === true) return true;
  }

  return false;
}

// checkPath("i", "l")

graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1],
};

/* 
Find number of connected paths
traverse through entire list of keys
Start depth/ breath traverse from keys
Add traversed nodes to set
If node exists exit traversal, skip entry? Dont traverse
Once traversal completed, increment count
*/
function connectedPaths() {
  let count = 0;
  let visited = new Set();

  for (const key in graph) {
    let src = Number(key);
    if (!visited.has(src)) {
      traverseConnectedPath(src, visited);
      count++;
    }
  }
  return count
}

function traverseConnectedPath(src, visited) {
  if (visited.has(src)) return;
  visited.add(src);

  for (const neigh of graph[src]) {
    traverseConnectedPath(neigh, visited);
  }
}

console.log(connectedPaths())