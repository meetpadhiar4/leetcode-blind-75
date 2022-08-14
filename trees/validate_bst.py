# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper_func(float('-inf'), root, float('inf'))
        
    def helper_func(self, min_val, root, max_val):
        if not root:
            return True
        if not (min_val < root.val < max_val):
            return False
        
        left = self.helper_func(min_val, root.left, root.val)
        right = self.helper_func(root.val, root.right, max_val)
        
        return left and right
