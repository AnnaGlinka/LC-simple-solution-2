from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []

        while root != None or stack != None:

            while root != None:
                stack.append(root)
                result.append(root.val)
                root = root.left

            if not stack:
                return result

            node = stack.pop()
            print("node=", node.val)
            root = node.right

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
