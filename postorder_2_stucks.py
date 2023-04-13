from typing import Optional, List
#https://leetcode.com/problems/binary-tree-postorder-traversal/

# 1. Push root to first stack.
# 2. Loop while first stack is not empty
#    2.1 Pop a node from first stack and push it to second stack
#    2.2 Push left and right children of the popped node to first stack
# 3. Print contents of second stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:   
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        s1 = []
        s2 = []
        if root is None:
            return []
        s1.append(root)
        while s1:
            parent = s1.pop()
            s2.append(parent)
            if parent.left:
                s1.append(parent.left)
            if parent.right:
                s1.append(parent.right)

        while s2:
            result.append(s2.pop().val)
            
        return result   
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(10)


root2 = TreeNode(1)
root2.right = TreeNode(2)
root.right.left = TreeNode(3)

root3 = TreeNode(None)


s = Solution()
print(s.postorderTraversal(root3))
