class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        LEETCODEISHIRING
        012345
        
        L     D     R
        E   O E   I I
        E C   I H   N
        T     S     G
        """
        # a = [
        #     ['L', ' ', ' ', 'D', ' ', ' ', 'R'],
        #     ['E', ' ', 'O', 'E', ' ', 'I', 'I']
        #     ]
        l = len(s)
        if numRows == 1:
            return s
        t = l // (numRows + numRows - 2)
        tt = (l % (numRows + numRows - 2)) % numRows +1
        la = t*2+tt
        a = [['' for i in range(la)] for i in range(numRows)]
        j = 0
        m = 1
        n = 0
        #按规律放到二维数组，按顺序输出数组
        for i in range(len(s)):
            while j < numRows and j >= 0 and n < l:
                a[j][i] = s[n]
                print(a)
                n += 1
                # print(a)
                j += m
            m *= -1
            j += m*2
        return ''.join([i for item in a for i in item if i != ''])

# print(Solution.convert(Solution, 'LEETCODEISHIRING', 4))
print(Solution.convert(Solution, 'LEETCODEISHIRING', 4))