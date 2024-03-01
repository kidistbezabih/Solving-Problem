# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        def search(node,val):
            nonlocal res
            if not node:
                return
            
            if node.val <  val:
                node = search(node.right, val)
            elif node.val > val:
                node = search(node.left, val)
            else:
                res =  node
                return
        search(root, val)
        return res
    