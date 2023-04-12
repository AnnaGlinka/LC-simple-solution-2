from typing import Optional, List
#https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    post = []
    def postorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            self.post.append(root.val)

        return self.post
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.post = [] #the same class is used a couple of times
        return self.postorder(root)
        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(10)


s = Solution()
print(s.postorderTraversal(root))
