class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper_func(n, {})
        
    def helper_func(self, n, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in memo:
            return memo[n]
        two_step = self.helper_func(n - 2, memo)
        one_step = self.helper_func(n - 1, memo)
        memo[n] = two_step + one_step
        
        return memo[n]
