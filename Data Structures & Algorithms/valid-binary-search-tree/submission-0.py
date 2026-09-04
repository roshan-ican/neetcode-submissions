# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, minimum, maximum):
            if node is None:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            left = check(node.left, minimum, node.val)
            right = check(node.right, node.val, maximum)

            return left and right

        return check(root, float("-inf"), float("inf"))
