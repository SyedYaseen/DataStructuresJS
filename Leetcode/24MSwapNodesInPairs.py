class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_nodes(head):
    curr = head
    print()
    print("Printing Linked List")
    while curr != None:
        print(curr.val)
        curr = curr.next


# ll_arr = [ll1]
Lls = []
# for i in ll_arr:
#     head = None
#     tail = None
#     for j in i:
#         if head is None:
#             head = ListNode(j)
#             tail = head
#         else:
#             tail.next = ListNode(j)
#             tail = tail.next
#     Lls.append(head)


def createLl(arr):
    head = None
    tail = None
    for j in arr:
        if head is None:
            head = ListNode(j)
            tail = head
        else:
            tail.next = ListNode(j)
            tail = tail.next
    return head


ll_arr1 = [1, 2, 3, 4]
LinkedList1 = createLl(ll_arr1)


class Solution(object):
    def func(self, head):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        current = head
        index = 0
        prev = None
        tail = None

        while current != None:
            if index == 0:
                tail = prev
                prev = current
                current = current.next
                index = 1
                continue

            if index == 1:
                temp = current
                prev.next = temp.next
                temp.next = prev

                if tail is None:
                    head = current
                else:
                    tail.next = current
                current = prev.next
                index = 0

        return head

    def func2(self, head):
        return self.swap(head)

    def swap(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        temp = head.next
        head.next = temp.next
        temp.next = head

        head.next = self.swap(head.next)

        return temp


sln = Solution()


print_nodes(sln.func(LinkedList1))
