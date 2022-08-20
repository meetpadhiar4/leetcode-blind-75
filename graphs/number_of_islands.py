class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, count = set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.helper_func(i, j, grid, visited):
                    count += 1
        
        return count
        
    def helper_func(self, i, j, grid, visited):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or (i, j) in visited or grid[i][j] == '0':
            return False
        visited.add((i, j))
        self.helper_func(i + 1, j, grid, visited)
        self.helper_func(i - 1, j, grid, visited)
        self.helper_func(i, j - 1, grid, visited)
        self.helper_func(i, j + 1, grid, visited)
        
        return True
