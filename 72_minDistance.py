# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符
#  
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/edit-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]表示：长度为i的word1转换成长度为j的word2所需的操作数
        # word1与word2相等 dp[i][j] = dp[i-1][j-1]
        # word1 替换一个字符变成word2 dp[i][j] = dp[i-1][j-1] + 1
        # word1 删除一个字符变成word2 dp[i][j] = dp[i-1][j] + 1
        # word1 添加一个字符变成word2 dp[i][j] = dp[i][j-1] + 1
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1
        dp = [[0 for i in range(l2+1)] for i in range(l1+1)]
        # i= 0 即word1为空
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] + 1
        # j=0 即word2为空
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[l1][l2]
print(Solution().minDistance("a", ""))
print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("intention", "execution"))