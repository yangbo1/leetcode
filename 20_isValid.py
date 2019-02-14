class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {'(': ")", "[": "]", "{": "}"}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if dict[stack.pop()] != i:
                    return False
        return len(stack)==0
s = Solution()
print(s.isValid('}'))