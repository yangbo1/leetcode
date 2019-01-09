class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 1:
            return s
        # def isPali(t):
        #     for i in range(len(t)):
        #         if t[i] == t[-i-1]:
        #             continue
        #         else:
        #             return False
        #     return True
        #
        # i, j = 0, l - 1
        # r = ''
        # lr = 0
        # while i < l-1:
        #     if j-i < lr:
        #         i += 1
        #         j = l - 1
        #     else:
        #         if isPali(s[i:j + 1]):
        #             r = s[i:j + 1]
        #             lr = len(r)
        #         else:
        #             j -= 1
        #         if j < i:
        #             i += 1
        #             j = l - 1
        # return r
        r = ''
        start = 0
        end = 0
        # 中心扩展算法，O(n²)
        for i in range(1,l):
            # i从1开始，已i为中心，判断i左右是否相等，相等就继续扩展，不相等i往后走，统计最长的子串
            k = 1
            while i >= k and i+k-1 < l:
                if s[i-k] == s[i+k-1]:
                    # tr = s[i-k:i+k]
                    # if len(tr) > len(r):
                    #     r = tr
                    if 2 * k > end - start:
                        start = i - k
                        end = i + k
                    k += 1
                else:
                    break
            j = 0
            #因为1221这样的中心在22的中间，所以还需要额外判断偶数的回文
            while i >= j and i + j < l:
                if s[i-j] == s[i+j]:
                    # tr = s[i-j:i+j+1]
                    # if len(tr) > len(r):
                    #     r = tr
                    if 2*j+1 > end-start:
                        start = i-j
                        end = i+j+1
                    j += 1
                else:
                    break
        return s[start:end]


print(Solution.longestPalindrome(Solution, "cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"))
# print(Solution.longestPalindrome(Solution, "ccc"))
