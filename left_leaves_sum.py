from typing import Optional 
#https://leetcode.com/problems/sum-of-left-leaves/
#O(n)
#O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        stuck = []
        if root is not None:
            stuck.append(root)
        while stuck:
            current = stuck.pop()
               
            if current.left is not None:
                stuck.append(current.left)
                
                if current.left.left is None and current.left.right is None:
                    sum += current.left.val
                    
            if current.right is not None:
                stuck.append(current.right)

        return sum
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(9)


s = Solution()
print(s.sumOfLeftLeaves(root))