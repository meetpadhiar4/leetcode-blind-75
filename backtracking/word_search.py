class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if self.helper_func(i, j, 0, board, word, visited):
                        return True
        
        return False
    
    def helper_func(self, i, j, k, board, word, visited):
        if k == len(word):
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != word[k] or (i, j) in visited:
            return False
        visited.add((i, j))
        res = self.helper_func(i + 1, j, k + 1, board, word, visited) or self.helper_func(i - 1, j, k + 1, board, word, visited) or self.helper_func(i, j + 1, k + 1, board, word, visited) or self.helper_func(i, j - 1, k + 1, board, word, visited)
        visited.remove((i, j))
        
        return res
