class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = []
        for i in range(len(nums)):
            tmp1 = target - nums[i]
            dict = {}
            for j in range(i+1, len(nums)):
                # print(dict)
                tmp2 = tmp1 - nums[j]
                if dict.__contains__(tmp2) and dict[tmp2] != j:
                        return target
                        # print([c,b,a])
                else:
                    dict.update({nums[j]: j})
        return r
s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], -1))