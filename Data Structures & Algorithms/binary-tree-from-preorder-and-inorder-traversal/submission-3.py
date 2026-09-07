# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order = {}
        for i, n in enumerate(inorder):
            in_order[n] = i

        pre_order_index = 0
        def build(left, right):
            nonlocal pre_order_index

            if left > right:
                return None 
            root_val = preorder[pre_order_index]
            pre_order_index += 1

            root = TreeNode(root_val)
            middle = in_order[root_val]

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root
        return build(0, len(inorder) - 1)