"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, ans):
            if not root:
                return 0
            for child in root.children:
                ans = max(ans, self.maxDepth(child) + 1)
            return ans

        return dfs(root, 1)
            
        