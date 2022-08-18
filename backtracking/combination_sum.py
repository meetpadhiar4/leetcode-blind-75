class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper_func(0, candidates, [], res, target)
        return res
        
    def helper_func(self, i, nums, path, res, target):
        if target == 0:
            res.append(path.copy())
            return 
        
        for j in range(i, len(nums)):
            if nums[j] <= target:
                path.append(nums[j])
                target -= nums[j]
                self.helper_func(j, nums, path, res, target)
                path.pop()
                target += nums[j]
