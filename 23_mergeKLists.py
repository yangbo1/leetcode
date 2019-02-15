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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            if l1 is None and l2 is None:
                return None
            if l1 is None and l2 is not None:
                return l2
            if l1 is not None and l2 is None:
                return l1
            if l1.val > l2.val:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2
            else:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
        if len(lists) == 0:
            return None
        t = lists[0]
        for i in range(1, len(lists)):
            t = mergeTwoLists(t, lists[i])
        return t
s = Solution()
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
list = []
list.append(l1)
list.append(l2)
list.append(l3)
show(s.mergeKLists(list))
