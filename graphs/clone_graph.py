"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node       
        d = defaultdict(Node)
        
        return self.helper_func(node, d)
              
    def helper_func(self, node, d):
        if node in d:
            return d[node]
        d[node] = Node(node.val)
        
        for nei in node.neighbors:
            d[node].neighbors.append(self.helper_func(nei, d))
            
        return d[node]
        
