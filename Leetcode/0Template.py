class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ll1 = [1, 4, 5]
ll2 = [1, 3, 4]
ll3 = [2, 6]

ll_arr = [ll1, ll2, ll3]
Lls = []
for i in ll_arr:
    head = None
    tail = None
    for j in i:
        if head is None:
            head = ListNode(j)
            tail = head
        else:
            tail.next = ListNode(j)
            tail = tail.next
    Lls.append(head)


class Solution(object):
    def func(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = None

        return res


sln = Solution()
print(sln.func([2, 7, 11, 15], 9))
