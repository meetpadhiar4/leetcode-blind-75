class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        return self.helper_func(0, s, word_dict, {})
        
    def helper_func(self, start, s, word_dict, memo):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        
        for i in range(start, len(s)):
            if s[start:i + 1] in word_dict and self.helper_func(i + 1, s, word_dict, memo):
                memo[start] = True
                return memo[start]
            
        memo[start] = False
        return memo[start]
        
