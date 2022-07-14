class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        max_streak = 0
        for num in s:
            if num - 1 not in s:
                curr_streak = 0
                curr = num - 1
                while curr + 1 in s:
                    curr_streak += 1
                    curr += 1
                max_streak = max(max_streak, curr_streak)
        
        return max_streak