# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if root and left or right is like doesn't have like difference of one
        # then tree is not balanced
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True

        left_height = height(root.left)
        right_height = height(root.right)

        # FIXED: abs(left_height - right_height)
        return (abs(left_height - right_height) <= 1 and
                self.isBalanced(root.left) and
                self.isBalanced(root.right))
    