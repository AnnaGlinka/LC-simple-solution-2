from typing import Optional
# O(N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)               
        return False


s = Solution()
p = TreeNode(1)
p.right = TreeNode(2)
p.left = TreeNode(3)


q = TreeNode(1)
q.right = TreeNode(2)
q.left = TreeNode(3)

print(s.isSameTree(p, q))