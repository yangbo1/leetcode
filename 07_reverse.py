class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
         [−231,  231 − 1]
        """
        if x < 0:
            sx = str(x*-1)
        else:
            sx = str(x)
        sr = ''
        #转成字符串倒叙遍历
        for i in range(1, len(sx)+1):
            sr += sx[-i]
        r = int(sr)
        if r > pow(2, 31)-1 or r < pow(-2, 31):
            return 0
        else:
            if x < 0:
                return r*-1
            else:
                return r
print(Solution.reverse(Solution, 1534236469))