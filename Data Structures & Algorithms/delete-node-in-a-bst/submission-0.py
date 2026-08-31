
class Solution:
    def getSuccessor(self, curr: Optional[TreeNode]):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            succ = self.getSuccessor(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root
