class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper_func(0, 0, text1, text2, {})
        
    def helper_func(self, i, j, text1, text2, memo):
        if i == len(text1) or j == len(text2):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + self.helper_func(i + 1, j + 1, text1, text2, memo)
            return memo[(i, j)]
        
        case_1 = self.helper_func(i + 1, j, text1, text2, memo)
        case_2 = self.helper_func(i, j + 1, text1, text2, memo)
        memo[(i, j)] = max(case_1, case_2)
        
        return memo[(i, j)]
