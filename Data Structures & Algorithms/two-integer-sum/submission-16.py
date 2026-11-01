class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            total = target - nums[i]
            if total in hashmap:
                return [hashmap[total], i]
            hashmap[nums[i]] = i