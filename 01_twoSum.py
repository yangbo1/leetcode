class Solution:
    def twoSum(self, nums, target):

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
        numsTmp = {}
        # for i in range(len(nums)):
        #   numsTmp.update({nums[i]: i})
        for i in range(len(nums)):
            # print(i, numsTmp[i])
            tmp = target - nums[i]
            # 如果字典中存在且下标不一样(不是同一个数字)
            if numsTmp.__contains__(tmp) and numsTmp[tmp] != i:
                # 两个值相等的下标
                return [numsTmp[tmp], i]
            # 存入字典 {值，下标}
            numsTmp.update({nums[i]: i})
if __name__ == '__main__':
    print(Solution.twoSum(Solution, [1, 3, 3], 6))