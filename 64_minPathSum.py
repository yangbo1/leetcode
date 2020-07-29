#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp = [[0 for i in grid[0]] for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                if i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                if i*j != 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[len(grid)-1][len(grid[0])-1]
print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))