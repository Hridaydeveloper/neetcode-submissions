class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return nums[i]
            hashmap[nums[i]] = i