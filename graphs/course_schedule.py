class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        curr_dfs = [0] * numCourses
        graph = defaultdict(list)
        for i in prerequisites:
            graph[i[0]].append(i[1])
        
        for i in range(0, numCourses):
            if visited[i] == 0:
                if not self.dfs(i, graph, visited, curr_dfs):  
                    return False
                    
        return True

    def dfs(self, node, graph, visited, curr_dfs):
        visited[node] = 1
        curr_dfs[node] = 1
        for nei in graph[node]:
            if visited[nei] == 0:
                if not self.dfs(nei, graph, visited, curr_dfs):
                    return False
            else:
                if curr_dfs[nei] == 1:
                    return False
        curr_dfs[node] = 0
        
        return True
