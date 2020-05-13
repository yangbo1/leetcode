# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def nextPermutation(self, nums):
        r = len(nums)-1
        l = r-1
        flag = True
        while l >= 0:
            if nums[l] < nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                ll= l + 1
                rr = len(nums)-1
                while ll < rr:
                    print(ll, rr, nums)
                    nums[ll], nums[rr] = nums[rr], nums[ll]
                    ll += 1
                    rr -= 1
                print(nums)
                flag = False
                break
            else:
                if r-l>1:
                    r -= 1
                else:
                    l -= 1
                    r = len(nums) -1
        if flag:
            ll = l + 1
            rr = len(nums) - 1
            while ll < rr:
                print(ll, rr, nums)
                nums[ll], nums[rr] = nums[rr], nums[ll]
                ll += 1
                rr -= 1
            print(nums)
# Solution().nextPermutation([7,1,2,6,5,4,3])
Solution().nextPermutation([9,8,7,6,44,55,66,10,5,4,3,2,1])
