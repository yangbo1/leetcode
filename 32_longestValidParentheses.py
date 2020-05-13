# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    #TODO
    def longestValidParentheses(self, s):
        print(s)
        l = len(s)
        if l <= 1:
            return 0
        stack = []

        i = 0
        result = 0
        while i < l:
            print(stack)
            if s[i] == "(":
                stack.append("(")

                i += 1
            else:
                if len(stack) == 0:
                    return max(result, self.longestValidParentheses(s[i+1:len(s)]))
                else:
                    stack.pop()
                    i += 1
                    result += 2
        return result
print(Solution().longestValidParentheses("()(((((()"))
# print(Solution().longestValidParentheses("()(()()))(((((((((()))))))))"))