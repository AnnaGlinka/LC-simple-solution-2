from typing import Optional, List
#https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/933036762/

# Create an empty stack nodeStack and push root node to stack. 
# Do the following while nodeStack is not empty. 
# Pop an item from the stack and print it. 
# Push right child of a popped item to stack 
# Push left child of a popped item to stack


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        if root is None:
            return result
        stack.append(root)
        while stack:
            parent = stack.pop()
            result.append(parent.val)
            if parent.right:
                stack.append(parent.right)
            if parent.left:
                stack.append(parent.left)
        return result
            

    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
print(s.preorderTraversal(root))

root2 = TreeNode(5)
root2.right = TreeNode(6)
root2.right.left = TreeNode(7)
print(s.preorderTraversal(root2))
