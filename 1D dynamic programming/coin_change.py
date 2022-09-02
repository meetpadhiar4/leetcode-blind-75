class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.helper_func(coins, amount, {})
        return res if res != float('inf') else -1
        
    def helper_func(self, coins, target, memo):
        if target == 0:
            return 0
        if target in memo:
            return memo[target]
        
        min_val = float('inf')
        for i in coins:
            if i <= target:
                min_val = min(min_val, 1 + self.helper_func(coins, target - i, memo))
        memo[target] = min_val
        
        return memo[target]
