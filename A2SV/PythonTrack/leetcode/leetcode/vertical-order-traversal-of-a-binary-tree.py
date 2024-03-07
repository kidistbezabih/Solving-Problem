# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dct = defaultdict(list)

        def traverse(row, col,root):
            if not root: 
                return None
            dct[col].append([row, root.val])
            traverse(row+1, col-1, root.left)
            traverse(row+1, col+1, root.right)

        traverse(0, 0, root)
        dct = dict(sorted(dct.items()))
        key = sorted(dct.keys())

        ans = []
        for i in key:
            level = []
            st = sorted(dct[i])
            for j in st:
                level.append(j[1])
            ans.append(level)
        return ans
            
