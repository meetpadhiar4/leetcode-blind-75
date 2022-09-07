class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper_func(0, 0, m, n, {})
        
    def helper_func(self, i, j, m, n, memo):
        if i == m or j == n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        right = self.helper_func(i, j + 1, m, n, memo)
        down = self.helper_func(i + 1, j, m, n, memo)
        memo[(i, j)] = right + down
        
        return memo[(i, j)]
