# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(node):
            if node:
                mx =1+ max(max_depth(node.left), max_depth(node.right))
                return mx
            else:
                return 0
        return max_depth(root)
