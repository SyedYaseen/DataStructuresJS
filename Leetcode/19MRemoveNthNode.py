# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l5 = ListNode(5)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5

l1 = ListNode(1)
l2 = ListNode(2)
# l3 = ListNode(3)
l1.next = l2
# l2.next = l3


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None or (head.next is None and n == 1):
            return None

        current = head
        size = 0

        while current is not None:
            current = current.next
            size += 1

        k = size - n
        i = 0

        if size == 2 and n == 2:
            head = head.next
            return head

        current = head
        while i < k - 1:
            current = current.next
            i += 1
        toRemove = current.next
        current.next = toRemove.next
        return head


s = Solution()
sol = s.removeNthFromEnd(l1, 2)
cur = sol
while cur is not None:
    print(cur.val)
    cur = cur.next
