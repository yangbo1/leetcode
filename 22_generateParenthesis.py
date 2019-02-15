class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # def isValid(s):
        #     stack = []
        #     for i in s:
        #         if i == '(':
        #             stack.append(i)
        #         else:
        #             if len(stack) == 0 or stack.pop() != '(':
        #                 return False
        #     return len(stack)==0
        # re = []
        # def perm(s, p, r):
        #     if p == r:
        #         if isValid(s):
        #             rs = "".join(s)
        #             if rs not in re:
        #                 re.append(rs)
        #     else:
        #         for i in range(p, r):
        #             s[i], s[p] = s[p], s[i]
        #             perm(s, p+1, r)
        #             s[i], s[p] = s[p], s[i]
        # s = []
        # for i in range(n):
        #      s.append("(")
        #      s.append(")")
        # perm(s, 0, 2*n-1)
        # return re

        #回溯法
        #只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像方法一那样每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
        #如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
        re = []
        def backtrack(s, l, r):
            if len(s) == 2*n:
                re.append(s)
                return
            if l < n:
                backtrack(s+'(', l+1, r)
            if l > r:
                backtrack(s+')', l, r+1)
        backtrack('', 0, 0)
        return re
s = Solution()
print(s.generateParenthesis(6))