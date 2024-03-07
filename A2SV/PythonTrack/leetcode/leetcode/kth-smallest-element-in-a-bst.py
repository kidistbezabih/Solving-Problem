# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        res = 0

        def inorder(root):
            nonlocal index
            nonlocal res

            if not root:
                return None
            inorder(root.left)
            index += 1
            if index == k:
                res = root.val
                return
            inorder(root.right)
            
        inorder(root)
        return res
