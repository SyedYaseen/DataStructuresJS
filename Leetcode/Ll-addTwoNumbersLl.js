class node {
  constructor(data) {
    this.data = data
    this.next = null
  }
}

class LinkedList {
  size = 0

  constructor(head = null) {
    this.head = head
    this.size = 1
  }

  appendNode(newNode) {
    let node = this.head
    if (node == null) {
      this.head = newNode
      this.size += 1
      return
    }
    while (node.next) {
      node = node.next
    }
    node.next = newNode
    this.size += 1
  }

  traverse() {
    let current = this.head
    let count = 0
    if (current === null) {
      console.log("Empty linkedlist")
    }
    while (current !== null) {
      let result = current.data
      count += 1
      current = current.next
      console.log(`${count}: ${result}`)
    }
  }

  getKthNode(k) {
    let current = this.head
    if (current === null) throw new Error("Empty linkedList")
    if (k > this.size) throw new Error("Index doesnt exist")

    while (current !== null && k >= 0) {
      if (k === 0) return current.data
      current = current.next
      k--
    }
  }
}

ll1 = new LinkedList(new node(2))
ll1.appendNode(new node(4))
ll1.appendNode(new node(3))

ll2 = new LinkedList(new node(5))
ll2.appendNode(new node(6))
ll2.appendNode(new node(4))

const twoSum = (l1, l2) => {
  current1 = l1.head
  current2 = l2.head
  let carry = 0
  let result = new LinkedList()

  while (current1 !== null || current2 !== null) {
    let sum = current1.data + current2.data + carry

    if (sum >= 10) {
      result = result.appendNode(new node(sum - 10))
      carry = 1
    } else {
      result = result.appendNode(new node(sum))
      carry = 0
    }

    current1 = current1.next
    current2 = current2.next
  }
  return result
}

let result = twoSum(ll1, ll2)
console.log(result.traverse())

// let a = new LinkedList()
// a.appendNode(new node(5))
// console.log(a)
