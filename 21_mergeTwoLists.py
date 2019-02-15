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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t = ListNode(None)
        r = t
        while l1 is not None or l2 is not None:
            if l1 is None and l2 is not None:
                t.next = l2
                break
            if l2 is None and l1 is not None:
                t.next = l1
                break
            if l2.val <= l1.val:
                t.next = ListNode(l2.val)
                t = t.next
                l2 = l2.next
            else:
                t.next = ListNode(l1.val)
                t = t.next
                l1 = l1.next
        return r.next
s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
show(s.mergeTwoLists(l1, l2))