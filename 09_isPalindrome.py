class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # x = str(x)
        # for i in range(len(x)):
        #     if x[i] == x[-i-1]:
        #         continue
        #     else:
        #         return False
        # return True
        elif x%10 == 0 and x != 0:
            # 末尾是0的情况只有0才是回文
            return False
        a = 0
        #取出一半数字，123321 123 = 123
        #1233321 1233 = 123  /10特殊处理
        while a < x:
            a = x%10 + a
            x = x//10
            # print(a, b)
            if a >= x:
                break
            a *= 10
        print(a,x)
        return a == x or a//10 == x
print(Solution.isPalindrome(Solution, 12321))