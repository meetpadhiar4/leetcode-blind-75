class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d:
                return [i, d[comp]]
            d[nums[i]] = i
        