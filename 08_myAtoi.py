class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        r = ''
        for i in range(len(str)):
            if str[i] == ' ' and len(r) == 0:
                continue
            if (str[i] == '-' or str[i] == '+') and len(r) == 0:
                r += str[i]
                continue
            if str[i].isdigit():
                r += str[i]
            else:
                break
        if len(r) == 0 or r == '-' or r == '+':
            return 0
        r = int(r)
        max = pow(2, 31)-1
        min = pow(-2, 31)
        if r > max:
            return max
        elif r < min:
            return min
        else:
            return r
print(Solution.myAtoi(Solution, '     +0 123'))