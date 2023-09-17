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

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val
  this.next = next === undefined ? null : next
}

let ll1 = new ListNode(2, new ListNode(4, new ListNode(3)))
let ll2 = new ListNode(5, new ListNode(6, new ListNode(4)))

ll1 = new ListNode(2, new ListNode(4, new ListNode(3, new ListNode(9))))

const twoSum = (l1, l2) => {
  let carry = 0
  let dummyHead = new ListNode(0)
  let tail = dummyHead

  while (l1 !== null || l2 !== null || carry !== 0) {
    if (l1 === null) l1 = new ListNode(0)
    if (l2 === null) l2 = new ListNode(0)

    let sum = l1.val + l2.val + carry

    if (sum >= 10) {
      sum = sum - 10
      carry = 1
    } else {
      carry = 0
    }

    newNode = new ListNode(sum)
    tail.next = newNode
    tail = tail.next

    l1 = l1.next
    l2 = l2.next
  }
  return dummyHead.next
}

let result = twoSum(ll1, ll2)
console.log(result)

