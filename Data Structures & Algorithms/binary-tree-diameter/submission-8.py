# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.d = 0
        self.height(root)
        return self.d
    
    def height(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)

        self.d = max(self.d, left + right + 2)

        return 1 + max(left, right)