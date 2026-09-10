class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        keys = list(hashmap.keys())
        keys.sort(key = lambda x: hashmap[x], reverse = True)
        res = []
        count = 0
        for key in keys:
            if count < k:
                res.append(key)
                count += 1
        return res