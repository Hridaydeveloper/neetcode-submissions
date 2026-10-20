class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)

        if length % 2 != 0:
            i = length // 2
            return nums[i]
        else:
            i = length // 2
            return (nums[i-1] + nums[i]) / 2

        


        