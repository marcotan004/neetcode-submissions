class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if len(nums) <= 1:
            return False
        
        prev = nums[0]
        for (i, n) in enumerate(nums):
            if i == 0:
                continue
            
            if prev == n:
                return True
            
            prev = n
        
        return False
            
            
