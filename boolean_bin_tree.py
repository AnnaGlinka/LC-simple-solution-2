#https://leetcode.com/problems/evaluate-boolean-binary-tree/
#leaf_node = {1: True, 0:False}
#non_leaf_node = {2: or, 3: and}
#O(n)
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
  
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return bool(root.val)

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 3:
            return left and right
        else:
            return left or right
                    
                     

#root = [2,1,3,null,null,0,1]

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

s = Solution()
print(s.evaluateTree(root))