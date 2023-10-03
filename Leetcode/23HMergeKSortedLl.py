# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_nodes(self, head):
        curr = head
        print()
        print("Printing Linked List")
        while curr != None:
            print(curr.val)
            curr = curr.next


ll1 = [1, 4, 5]
ll2 = [1, 3, 4]
ll3 = [2, 6]


llis1 = [ll1, ll2, ll3]
ll4 = [[], [1]]
Lls = []
for i in llis1:
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
    def func(self, lls):
        res = None
        tail = None
        index = 0
        smallest = None
        indexOfSmallest = None

        while (len(lls) > 0):
            if len(lls) == 1:
                if res is None:
                    res = lls[0]
                    return res
                if res is not None:
                    tail.next = lls[0]
                    return res

            if index > len(lls):
                index = 0

            if lls[index] == None:
                del lls[index]
                continue

            current_val = lls[index].val

            if smallest == None or current_val <= smallest:
                smallest = current_val
                indexOfSmallest = index

            if index == len(lls) - 1:
                node = ListNode(smallest)
                if res is None:
                    res = node
                    tail = res

                if res is not None:
                    tail.next = node
                    tail = tail.next

                lls[indexOfSmallest] = lls[indexOfSmallest].next

                if lls[indexOfSmallest] is None:
                    del lls[indexOfSmallest]
                else:
                    index += 1

                smallest = None

            index += 1
        return res

    def func2(self, lls):
        res = None
        tail = None
        arr = []
        for lst in lls:
            curr = lst
            while curr != None:
                arr.append(curr.val)
                curr = curr.next
        arr.sort()
        index = 0
        for i in arr:
            if index != 0:
                tail.next = ListNode(i)
                tail = tail.next
                continue
            else:
                res = ListNode(i)
                tail = res
                index += 1

        return res


sln = Solution()
# ListNode().print_nodes(sln.func(Lls))
result = sln.func2(Lls)
ListNode().print_nodes(result)
