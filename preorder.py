from typing import Optional, List
#O(n)


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre_list = []

    def transverse(self, node: Optional[TreeNode]):
        if node is not None:
            self.pre_list.append(node.val)
            self.transverse(node.left)
            self.transverse(node.right)

        return self.pre_list

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.pre_list = []
        return self.transverse(root)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.preorderTraversal(root))

root2 = TreeNode(5)
root2.right = TreeNode(6)
root2.right.left = TreeNode(7)
print(s.preorderTraversal(root2))
