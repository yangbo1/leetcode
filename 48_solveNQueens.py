# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
#
# 输入：n = 1
# 输出：[["Q"]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-queens
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = [['.' for i in range(n)] for i in range(n)]
        # print(res)
        result = []
        def check(i,j):
            # 判断是否能放置
            for p in range(n):
                for q in range(n):
                    if 'Q' == res[i][q] or 'Q' == res[p][j]:
                        return False
                    if p-q == i-j and 'Q' == res[p][q]:
                        return False
                    if p+q == i+j and 'Q' == res[p][q]:
                        return False
            return True
        def back(i):
            if i == n:
                print('结果',res)
                result.append([''.join(res[i]) for i in range(len(res))])
                return
            for j in range(n):
                print(res)
                if check(i,j):
                    res[i][j] = 'Q'
                    back(i+1)
                    res[i][j] = '.'
        back(0)
        return result
print(Solution().solveNQueens(4))
