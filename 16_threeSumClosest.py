class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        snums = sorted(nums)
        re = snums[0]+snums[1]+snums[2]
        for i in range(len(snums)):
            l = i+1
            r = len(snums)-1
            while(l < r):
                if abs(snums[i]+snums[l]+snums[r] - target) < abs(re-target):
                    re = snums[i]+snums[l]+snums[r]
                if snums[i]+snums[l]+snums[r] > target:
                    r -= 1
                elif snums[i]+snums[l]+snums[r] < target:
                    l += 1
                else:
                    return target
        return re
s = Solution()
# print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82))