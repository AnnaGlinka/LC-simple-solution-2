from typing import Optional 
#https://www.geeksforgeeks.org/find-sum-left-leaves-given-binary-tree/
#https://leetcode.com/problems/sum-of-left-leaves/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
   
    def is_leaf(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True
        return False

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        if root is not None:
            if self.is_leaf(root.left):
                sum += root.left.val
            else:
                sum += self.sumOfLeftLeaves(root.left)  
            sum += self.sumOfLeftLeaves(root.right)
        return sum
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)


s = Solution()
print(s.sumOfLeftLeaves(root))