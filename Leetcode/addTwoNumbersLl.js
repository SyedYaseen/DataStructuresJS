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

ll1 = new LinkedList(new node(2))
ll1.appendNode(new node(4))
ll1.appendNode(new node(3))

ll2 = new LinkedList(new node(5))
ll2.appendNode(new node(6))
ll2.appendNode(new node(4))

const traverse = (node) => {
  console.log(node.next)
  //   while (node.next) {
  //     console.log(node.data)
  //   }
}

traverse(ll1)
