# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = defaultdict(int)
        for i in range(len(inorder)):
            in_map[inorder[i]] = i
            
        return self.helper_func(0, len(inorder) - 1, inorder, 0, len(preorder) - 1, preorder, in_map)
            
    def helper_func(self, in_start, in_end, inorder, pre_start, pre_end, preorder, in_map):
        if pre_start > pre_end or in_start > in_end:
            return None
        root = TreeNode(preorder[pre_start])
        root_idx = in_map[root.val]
        nums_left = root_idx - in_start
        root.left = self.helper_func(in_start, root_idx - 1, inorder, pre_start + 1, pre_start + nums_left, preorder, in_map)
        root.right = self.helper_func(root_idx + 1, in_end, inorder, pre_start + nums_left + 1, pre_end, preorder, in_map)
        
        return root
