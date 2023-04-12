from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def symetric(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False
            else:
                return self.symetric(root1.left, root2.right) and self.symetric(root1.right, root2.left)
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.symetric(root, root):
            return True
        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)


s = Solution()
print(s.isSymmetric(root))