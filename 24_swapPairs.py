class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def show(l):
    while l.next is not None:
        print(l.val, end = '->')
        l = l.next
    print(l.val)
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(None)
        h.next = head
        p = h
        while p.next and p.next.next:
            tmp = p.next.next
            if tmp.next is not None:
                p.next.next = tmp.next
            else:
                p.next.next = None
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return h.next
s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
show(s.swapPairs(l))