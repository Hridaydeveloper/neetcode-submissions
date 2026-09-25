class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #Product of everything from left side
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product = product * nums[i]

        #Product of everything from right side
        product = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * product
            product = product * nums[i]
        return res