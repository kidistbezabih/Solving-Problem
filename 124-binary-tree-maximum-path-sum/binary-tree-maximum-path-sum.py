# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            ans = max(ans, (max(left, 0) + max(right, 0) + node.val))
            return max(max(right, 0) + node.val, max(left, 0) + node.val)
            
        dfs(root)
        return ans

            
