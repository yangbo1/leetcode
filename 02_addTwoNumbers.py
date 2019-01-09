# Definition for singly-linked list.
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # tmp1 = l1
        # tmp2 = l2
        # l1length = 0
        # l2length = 0
        # while tmp1 is not None:
        #     l1length += 1
        #     tmp1 = tmp1.next
        # while tmp2 is not None:
        #     l2length += 1
        #     tmp2 = tmp2.next
        # print(l1length)
        # print(l2length)
        # a = l1length - l2length
        # if a > 0:
        #     for i in range(0, a):
        #         addl = ListNode(0)
        #         addl.next = l2
        #         l2 = addl
        # elif a < 0:
        #     for i in range(0, abs(a)):
        #         addl = ListNode(0)
        #         addl.next = l1
        #         l1 = addl
        # # Solution.show(l1)
        # # Solution.show(l2)
        re = ListNode(0)
        r = re
        while l1 is not None or l2 is not None:
            sum = l1.val + l2.val
            # 1->2->3
            # 1->2->3->4
            if l1.next is None and l2.next is not None:
                # 添加一个0节点
                l1.next = ListNode(0)
                #sum进1
                if sum >= 10:
                    sum -= 10
                    l1.next.val += 1
            # 1->2->3->4
            # 1->2->3
            elif l2.next is None and l1.next is not None:
                l2.next = ListNode(0)
                if sum >= 10:
                    sum -= 10
                    l2.next.val += 1
            elif l1.next is None and l2.next is None:
                if sum >= 10:
                    sum -= 10
                    l1.next = ListNode(0)
                    l2.next = ListNode(0)
                    l1.next.val += 1
            else:
                if sum >= 10:
                    sum -= 10
                    l1.next.val += 1
            # l1 l2继续往后遍历
            l1 = l1.next
            l2 = l2.next
            r.next = ListNode(sum)
            r = r.next
        return re.next

        # return l1.val
if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(8)
    l1.next.next = ListNode(5)
    l1.next.next = ListNode(9)
    l2 = ListNode(1)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # Solution.show(Solution, l1)
    Solution.show(Solution.addTwoNumbers(Solution, l1, l2))
    # a = ListNode(0)
    # aa = a
    # for i in range(1,13):
    #     aa.next = ListNode(i)
    #     aa = aa.next
    # Solution.show(a)