class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def show(l):
        while l.next is not None:
            print(l.val, end = '->')
            l = l.next
        print(l.val)
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        count = 1
        #遍历一趟，p遍历n次时q开始走，p结束时，q的位置就是要删除的位置
        while p.next is not None:
            if count == n:
                q = head
            p = p.next
            if count > n:
                q = q.next
            count += 1
        if 'q' in dir():
            q.next = q.next.next
            return head
        else:
            return head.next
s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
Solution.show(s.removeNthFromEnd(l, 1))