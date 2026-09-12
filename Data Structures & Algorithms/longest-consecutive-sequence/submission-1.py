class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()
        k = nums[0]
        count = 0
        longest = 0
        for i in range(len(nums)):
            if nums[i] == k - 1:
                continue
            if nums[i] == k:
                count += 1
                longest = max(count, longest)
                k += 1
            else:
                count = 1
                k = nums[i] + 1
        return longest
        