class node {
  constructor(data) {
    this.data = data
    this.next = null
  }
}

class LinkedList {
  constructor(head = null) {
    this.head = head
  }

  appendNode(newNode) {
    let node = this.head
    if (node == null) {
      this.head = newNode
      return
    }
    while (node.next) {
      node = node.next
    }
    node.next = newNode
  }
}
