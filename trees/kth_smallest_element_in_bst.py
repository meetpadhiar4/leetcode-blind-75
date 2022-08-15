# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        self.res = None
        self.k = k
        self.helper_func(root, self.k, self.res)
        return self.res
        
    def helper_func(self, root, k ,res):
        if root:
            self.helper_func(root.left, k, res)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return 
            self.helper_func(root.right, k, res)
