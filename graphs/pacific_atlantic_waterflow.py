class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set, atlantic_set = set(), set()
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    self.helper_func(i, j, heights, heights[i][j], pacific_set)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    self.helper_func(i, j, heights, heights[i][j], atlantic_set)

        for i in pacific_set:
            if i in atlantic_set:
                res.append(list(i))
                
        return res
        
    def helper_func(self, i, j, heights, prev, visited):
        if i < 0 or i == len(heights) or j < 0 or j == len(heights[0]) or (i, j) in visited or heights[i][j] < prev:
            return 
        visited.add((i, j))
        self.helper_func(i + 1, j, heights, heights[i][j], visited)
        self.helper_func(i - 1, j, heights, heights[i][j], visited)
        self.helper_func(i, j + 1, heights, heights[i][j], visited)
        self.helper_func(i, j - 1, heights, heights[i][j], visited)
