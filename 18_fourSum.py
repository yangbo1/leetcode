class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #参考第一题两书之和，O(n³)很慢
        r = []
        for i in range(len(nums)):
            tmp1 = target - nums[i]
            for j in range(i+1, len(nums)):
                # print(dict)
                tmp2 = tmp1 - nums[j]
                dict = {}
                for k in range(j+1, len(nums)):
                    tmp3 = tmp2 - nums[k]
                    if dict.__contains__(tmp3) and dict[tmp3] != k:
                        a = nums[i]
                        b = tmp3
                        c = nums[j]
                        d = nums[k]
                        list = []
                        list.append(a)
                        list.append(b)
                        list.append(c)
                        list.append(d)
                        l = sorted(list)
                        if l not in r:
                            r.append(l)
                            # print([c,b,a])
                    else:
                        dict.update({nums[k]: k})

        return r
s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
# print(s.fourSum([-3,-1,0,2,4,5], 1))