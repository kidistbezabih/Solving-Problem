# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left, right):
            if not root:
                return True
            
            if root.val <= left or root.val >= right:
                return False

            if root.left:
                if not validate(root.left, left, root.val):
                    return False

            if root.right:
                if not validate(root.right, root.val, right):
                    return False

            return True

        return validate(root, float("-inf"), float("inf"))




        # def validate(current, lowerEnd, higherEnd):
        #     if current.val >= higherEnd:
        #         return False
            
        #     if current.val <= lowerEnd:
        #         return False
            
            
        #     if current.left:
        #         if not validate(current.left, lowerEnd, current.val):
        #             return False
            
        #     if current.right:
        #         if not validate(current.right, current.val, higherEnd):
        #             return False
            
        #     return True
            

        
        # return validate(root, float("-inf"), float("inf"))
