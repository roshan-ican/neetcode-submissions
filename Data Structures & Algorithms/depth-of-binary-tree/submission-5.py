# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we should like go too the function and count the nodes
        # if the left node has more or right has more 
        # which ever
        count = 0
        count2= 0
        if root is None:
            return 0
        if root.left:
            count = self.maxDepth(root.left)
        if root.right:
            count2 = self.maxDepth(root.right)


        res = 1+ max(count, count2)
        return res

        