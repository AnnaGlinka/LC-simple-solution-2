from typing import Optional, List
#https://leetcode.com/problems/binary-tree-postorder-traversal/
#https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def peek(self, stack: List[TreeNode]):
        if len(stack) > 0:
            return stack[-1]
        return None
     
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        if root is None:
            return result
      
        while True:
            while root is not None:
                print("root=", root.val)
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)

                root = root.left

            print("stack[-1]", len(stack))

            root = stack.pop()
            if len(stack) > 0:
                if (root.right is not None and stack[-1] == root.right):
                    stack.pop()
                    stack.append(root) 
                    root = root.right 

            else:
                result.append(root.val)
                root = None

            if len(stack) <= 0:
                break
                
        return result
        

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
