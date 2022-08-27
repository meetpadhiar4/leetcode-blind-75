class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper_func(nums, 0, {})
    
    def helper_func(self, nums, i, memo):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        take = nums[i] + self.helper_func(nums, i + 2, memo)
        not_take = self.helper_func(nums, i + 1, memo)
        memo[i] = max(take, not_take)
        
        return memo[i]
