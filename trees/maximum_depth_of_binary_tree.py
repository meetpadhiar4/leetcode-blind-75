# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper_func(root)
        
    def helper_func(self, root):
        if not root:
            return 0
        left = 1 + self.helper_func(root.left)
        right = 1 + self.helper_func(root.right)
        
        return max(left, right)
        
