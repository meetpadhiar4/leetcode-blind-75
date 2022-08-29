class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # excluding_last = self.helper_func(0, len(nums) - 2, nums, 0, {})
        # including_last = self.helper_func(1, len(nums) - 1, nums, 0, {})
        
        return max(self.helper_func(0, len(nums) - 2, nums, 0, {}), self.helper_func(1, len(nums) - 1, nums, 0, {}))
        
    def helper_func(self, start, end, nums, amount, memo):
        if start > end:
            return amount
        if (start, amount) in memo:
            return memo[(start, amount)]
        # take = self.helper_func(start + 2, end, nums, amount + nums[start], memo)
        # not_take = self.helper_func(start + 1, end, nums, amount, memo)
        memo[(start, amount)] = max(self.helper_func(start + 2, end, nums, amount + nums[start], memo), self.helper_func(start + 1, end, nums, amount, memo))
        
        return memo[(start, amount)]
