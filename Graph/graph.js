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
  return count;
}

function traverseConnectedPath(src, visited) {
  if (visited.has(src)) return;
  visited.add(src);

  for (const neigh of graph[src]) {
    traverseConnectedPath(neigh, visited);
  }
}

// console.log(connectedPaths())

/*
Find the largest component

Df through each node in object
Put nodes visited in a set - to avoid cyclic issues
Put all nodes part of one traversal in one set or increment a count variable
This would separate the connected nodes
*/
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2],
};

function largestComponent() {
  let visited = new Set();
  let numberOfComponents = 0;
  let components = {};
  let largestComponent = [];
  let sizeOfLargestComponent = 0;

  for (const key in graph) {
    let src = Number(key);
    let nodesInIteration = 0;
    if (!visited.has(src)) {
      numberOfComponents++;

      // traverse(src, visited, (node) => {
      //   components[numberOfComponents] === undefined
      //     ? (components[numberOfComponents] = [node])
      //     : (components[numberOfComponents] = [
      //         ...components[numberOfComponents],
      //         node,
      //       ]);
      // });

      // This check the largest component every iteration without
      // trying to do this again separately with another loop
      // if (largestComponent.length < components[numberOfComponents].length)
      //   largestComponent = components[numberOfComponents];

      //This only returns #of nodes, not the nodes themselves
      traverse(src, visited, () => nodesInIteration++);
      if (sizeOfLargestComponent < nodesInIteration)
        sizeOfLargestComponent = nodesInIteration;
    }
  }
  // console.log(largestComponent);
  console.log(sizeOfLargestComponent);
}

function traverse(src, visited, addToComponents) {
  if (visited.has(src)) return;
  visited.add(src);
  // addToComponents(src);
  addToComponents();
  for (const neigh of graph[src]) {
    traverse(neigh, visited, addToComponents);
  }
}

// largestComponent();
// Result - All components = { 0: [0, 8, 5, 1], 1: [2, 3, 4] };
// largest component = [ 0, 8, 5, 1 ]

/*
Find shortest path between two nodes
Depth first might not work as expected, because the chose direction might left to chance
Using breadth first would ensure that nodes are visited evenly on each direction --> not left to chance and shortest path is found efficietly

pseudo:
bf traversal
terminate if src = dest
else traverse neightbours and add them to queue
add visited nodes to set to avoid cyclic issues

increment counter to keep track of distance from source node and send with current node
return counter once src=dest
*/

graph = {};
edgeList = [
  ["w", "x"],
  ["x", "y"],
  ["z", "y"],
  ["z", "v"],
  ["w", "v"],
  ["x", "v"],
  ["z", "m"],
  ["m", "y"],
];

EgdeListToGraph(edgeList);
// console.log(graph);

function shortestPath(src, dest) {
  let q = [{ current: src, currentDistance: 0 }];
  let visited = new Set([src]);
  let shortestDistance = 0;

  //edge case where src and dest are the same when function is called
  if (src === dest) return shortestDistance;

  while (q.length > 0) {
    let { current, currentDistance } = q.shift();

    if (current === dest) {
      if (shortestDistance === 0) shortestDistance = currentDistance;
      if (currentDistance < shortestDistance)
        shortestDistance = currentDistance;
    }

    for (const neighbour of graph[current]) {
      if (!visited.has(neighbour)) {
        visited.add(neighbour);
        q.push({ current: neighbour, currentDistance: currentDistance + 1 });
      }
    }
  }

  return shortestDistance;
}

// console.log(shortestPath("x", "m"));

/*
Island count
*/
const grid = [
  ["W", "L", "W", "W", "W"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "L", "W"],
  ["W", "W", "L", "L", "W"],
  ["L", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "W"],
];

const islandCount = (grid) => {
  let visited = new Set()

  let rowLength = grid.length;
  for (let row = 0; row < rowLength; row++) {
    let colLength = grid[row].length;
    for (let column = 0; column < colLength; column++) {

      



      console.log(grid[row][column]);
    }
  }
};

islandCount(grid);
// let numberOfComponents = 0;
// let components = {};
// function test(node) {
//   console.log(components[numberOfComponents]);
//   components[numberOfComponents] === undefined
//     ? (components[numberOfComponents] = [node])
//     : (components[numberOfComponents] = [
//         ...components[numberOfComponents],
//         node,
//       ]);

//   numberOfComponents++;
// }
