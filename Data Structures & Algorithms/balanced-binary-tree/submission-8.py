# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        l = self.height(root.left)
        r = self.height(root.right)

        if abs(l - r) > 1:
            return False
        
        l_b = self.isBalanced(root.left)
        r_b = self.isBalanced(root.right)

        return l_b and r_b
    

    def height(self, root: Optional[TreeNode]) -> int:

        if not root:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)
        