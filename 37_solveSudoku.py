# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。
#
#
#
# 一个数独。
#
#
#
# 答案被标成红色。
#
# Note:
#
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sudoku-solver
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def solveSudoku(self, board):
        def isValid(i, j, k):
            if k in board[i] or k in [a[j] for a in board]:
                # print(i, j, k)
                return False
            for m in range(i//3*3, i//3*3+3):
                for n in range(j//3*3, j//3*3+3):
                    if board[m][n] == k:
                        # print(i, j, k)
                        return False
            return True
        def solve(i, j):
            if i>8 or j>8:
                return True
            if board[i][j] == ".":
                for k in range(1, 10):
                    # print(board)
                    if isValid(i, j, str(k)):
                        board[i][j] = str(k)
                        if j == 8:
                            if solve(i+1, 0):
                                return True
                        else:
                            if solve(i, j+1):
                                return True
                        board[i][j] = "."
            else:
                if j == 8:
                    if solve(i + 1, 0):
                        return True
                else:
                    if solve(i, j + 1):
                        return True
        solve(0,0)
        print(board)
s = Solution()
print(s.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
))
