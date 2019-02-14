class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def fun(s1, s2):
            r = []
            for m in s1:
                for n in s2:
                    r.append(m+n)
            return r
        if digits == '':
            return []
        s1 = list(dict[digits[0]])
        for i in range(1, len(digits)):
            s2 = dict[digits[i]]
            s1 = fun(s1, s2)
        return s1
s = Solution()
print(s.letterCombinations('8'))