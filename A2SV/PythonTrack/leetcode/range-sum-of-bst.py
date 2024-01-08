# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node):
            if node is None:
                return 0

            total = 0
            total += inorder(node.left)

            if low <= node.val <= high:
                total += node.val

            total += inorder(node.right)
            return total
        return inorder(root)