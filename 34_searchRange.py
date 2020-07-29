# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums)-1
        j, k = [-2, 0]
        while l <= r:
            i = l + (r-l)//2
            if nums[i] < target:
                l = i+1
            elif nums[i] > target:
                r = i-1
            else:
                j, k = i, i
                break

        while j >= 0:
            if nums[j] == target:
                j -= 1
            else:
                break
        while k < len(nums):
            if nums[k] == target:
                k += 1
            else:
                break
        return [j+1, k-1]
print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([1], 1))