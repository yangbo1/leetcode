class Solution:
    def isMatch(self, s, p):
        """

        :type s: str
        :type p: str
        :rtype: bool
        """
        # not fixed todo
        if '*' not in p and '.' not  in p and s != p:
            return False
        ls = len(s)
        lp = len(p)
        t = 0
        # while i < lp:
        j = 0
        # t = i
        while j < ls and t < lp:
            if s[j] == p[t] or p[t] == '.':
                if j == ls-1:
                    if t == lp - 1:
                        return True
                    else:
                        if set(p[t - 1:lp][1::2]) == {'*'} and p[lp - 1] == '*':
                            return True
                        else:
                            j-=1
                # print(s[j])
                j+=1
                t+=1
            elif p[t] == '*' and t>= 1:
                if s[j]==p[t-1] or p[t-1] == '.':
                    if j == ls-1:
                        if t == lp - 1:
                            return True
                        else:
                            if set(p[t-1:lp][1::2]) == {'*'} and p[lp-1] == '*':
                                return True
                            else:
                                j-=1
                                t+=1
                    # print(s[j])
                    j+=1
                else:
                    t+=1
            else:
                if t <lp -1 and p[t+1] == '*':
                    t+=1
                else:
                    return False
            # i+=1
        return False
# print(Solution.isMatch(Solution, 'mississippi', 'mis.is*ip*.'))
print(Solution.isMatch(Solution, 'aa', 'aaa*a'))