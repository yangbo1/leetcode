class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, -1, -1):
            if len(nums) == 1:
                return len(nums)
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)
s = Solution()
print(s.removeDuplicates([1,1,2,3,4]))