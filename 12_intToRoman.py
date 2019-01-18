class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        I 1
        IV 4
        V 5
        IX 9
        X 10
        XL 40
        L 50
        XC 90
        C 100
        CD 400
        D 500
        CM 900
        M 1000

        1994 = 1000+900+90+4 MCMXCIV
        """
        dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        a = num
        r =''
        for i in dict.keys():
            if a >= i:
                # print(a,i)
                b = a//i
                for j in range(b):
                    r += dict[i]
                a = a%i
        return r
s = Solution()
print(s.intToRoman(3999))