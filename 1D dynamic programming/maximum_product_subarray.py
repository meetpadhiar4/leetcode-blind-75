class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
          
        res, min_val, max_val = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = max_val
            max_val = max(nums[i], temp * nums[i], min_val * nums[i])
            min_val = min(nums[i], temp * nums[i], min_val * nums[i])
            res = max(res, max_val, min_val)
            
        return res
