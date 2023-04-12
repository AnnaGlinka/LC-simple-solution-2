from typing import Optional
# Time complexity : O(n)
# Space complexity : O(h) for recursion call stack, where h is the height of the tree.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invert(self, root: Optional[TreeNode]):
        if root is None:
            return
  
        root.right, root.left = root.left, root.right
        self.invert(root.left)
        self.invert(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            self.invert(root)
        return root


def print_preorder(root):
    if root is None:
        return
    print(root.val)
    print_preorder(root.left)
    print_preorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print_preorder(root)

s = Solution()
root1 = s.invertTree(root)
print("------------")

print_preorder(root1)
