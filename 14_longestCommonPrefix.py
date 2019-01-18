class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        i,j = 0,0
        r = ''
        while j < len(strs[0]):
            while i < len(strs)-1:
                if len(strs[i+1]) > j and strs[i][j] == strs[i+1][j]:
                    i += 1
                else:
                    return r
            r += strs[0][j]
            j += 1
            i = 0
        return r
s = Solution()
# print(s.longestCommonPrefix(["aflower","aflow","aflight"]))
print(s.longestCommonPrefix(['ab', 'ab', 'abab', 'ab']))