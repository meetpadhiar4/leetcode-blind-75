# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        
        return root
        
    def helper_func(self, root):
        if not root:
            return root
        left = self.helper_func(root.left)
        right = self.helper_func(root.right)
        root.left, root.right = root.right, root.left
        
        return root
