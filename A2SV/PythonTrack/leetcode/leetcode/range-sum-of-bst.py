# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def traverse(root):
            nonlocal total
            if not root:
                return 0
            if low <= root.val <= high:
                total += root.val 
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return total
            