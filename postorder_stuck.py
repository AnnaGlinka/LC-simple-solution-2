from typing import Optional, List
#https://leetcode.com/problems/binary-tree-postorder-traversal/

# 1.1 Create an empty stack
# 2.1 Do following while root is not NULL
#     a) Push root's right child and then root to stack.
#     b) Set root as root's left child.
# 2.2 Pop an item from stack and set it as root.
#     a) If the popped item has a right child and the right child 
#        is at top of stack, then remove the right child from stack,
#        push the root back and set root as root's right child.
#     b) Else print root's data and set root as NULL.
# 2.3 Repeat steps 2.1 and 2.2 while stack is not empty.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def print_stuck(self, stack: List[TreeNode]):
        print('currnet stack:')
        for elem in stack:
            print(elem.val, end=",")
        print()

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
            self.print_stuck(stack)       
            while root is not None:
               
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)

                root = root.left
               
            self.print_stuck(stack)       
            root = stack.pop()
            
          
            if (root.right is not None and self.peek(stack) == root.right):
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
