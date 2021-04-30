# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def back(d):
            if len(nums) == len(path):
                if path[:] not in res:
                    res.append(path[:])
                return
            for i in range(len(nums)):
                # print(d, path)
                if d[i] == 1:
                    continue
                path.append(nums[i])
                d[i] = 1
                back(d)
                path.pop()
                d[i] = 0
        back([0 for i in range(len(nums))])
        return res
print(Solution().permuteUnique([1,1,2]))
