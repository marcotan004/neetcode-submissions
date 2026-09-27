class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1 for i in nums]
        prefix = 1
        postfix = 1

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            postfix *= nums[len(nums) - i]
            ret[i] *= prefix
            ret[len(nums) - i - 1] *= postfix
        
        return ret
