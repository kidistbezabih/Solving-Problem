# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def left_nodes(root):
            if not root or (not root.left and not root.right):
                return
            
            left.append(root.val)
            if root.left:
                left_nodes(root.left)
            else:
                left_nodes(root.right)

        def right_nodes(root):
            if not root or (not root.left and not root.right):
                return
            
            right.append(root.val)
            if root.right:
                right_nodes(root.right)
            else:
                right_nodes(root.left)

        def leaf_nodes(root):
            if not root:
                return
            if not root.right and not root.left:
                leaf.append(root.val)
            if root.left:
                leaf_nodes(root.left)
            if root.right:
                leaf_nodes(root.right)
            

        left = []
        right = []
        leaf = []


        left_nodes(root.left)
        leaf_nodes(root.left)
        leaf_nodes(root.right)
        right_nodes(root.right)

        return [root.val] + left + leaf + right[::-1] 