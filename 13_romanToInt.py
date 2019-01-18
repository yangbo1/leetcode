class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
        #         5: 'V', 4: 'IV', 1: 'I'}
        dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        r = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if dict[s[i]] >= dict[s[i+1]]:
                    r += dict[s[i]]
                else:
                    r += dict[s[i:i+2]]
                    i += 1
            else:
                r += dict[s[i]]
            i += 1
        return r
s = Solution()
print(s.romanToInt('MCMXCIV'))