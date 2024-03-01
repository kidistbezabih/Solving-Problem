# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dictionary = defaultdict(int)

        def traverse(node):
            nonlocal dictionary
            if not node:
                return None
            dictionary[node.val] += 1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        _max = max(dictionary.values())
        return [i for i in dictionary if dictionary[i] == _max ]