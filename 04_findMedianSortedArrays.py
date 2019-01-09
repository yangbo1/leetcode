class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        re = nums1 + nums2
        r = sorted(re)
        l = len(r)
        if l%2 == 0:
            return (r[l//2] + r[l//2-1])/2
        else:
            return r[l//2]
print(Solution.findMedianSortedArrays(Solution, [1,2], [1, 4, 5]))