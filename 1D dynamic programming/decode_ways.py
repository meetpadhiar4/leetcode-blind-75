class Solution:
    def numDecodings(self, s: str) -> int:
        return self.helper_func(0, s, {})
        
    def helper_func(self, start, s, memo):
        if start == len(s):
            return 1
        if start in memo:
            return memo[start]
        
        res = 0
        for i in range(start, len(s)):
            if int(s[start:i + 1]) <= 26 and s[start] != '0':
                res += self.helper_func(i + 1, s, memo)
        memo[start] = res
                
        return memo[start]
