class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl = len(needle)
        hl = len(haystack)
        if nl == 0:
            return 0
        if hl < nl:
            return -1
        for i in range(hl-nl+1):
            if needle == haystack[i:i+nl]:
                return i
        return -1
print(Solution().strStr("432143124554325258hwehrb293uibrf934t4322122b39ufb2934u2309hfjnajhrou23h4013rtjbjk34t43212", "34t432212"))