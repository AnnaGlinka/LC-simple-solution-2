from typing import Optional, List

#https://leetcode.com/problems/binary-tree-paths/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    path_list = []

    def add_path(self, path: str):
        self.path_list.append(path)

    def is_leaf(self, node: Optional[TreeNode]) -> bool:
        if node.left is None and node.right is None:
            return True
        return False

    def get_path(self, root: Optional[TreeNode], path: str):
        if root is None:
            return self.path_list
        if self.is_leaf(root):
            path += str(root.val)
            self.add_path(path)
            #print(self.path_list)
        else:
            path += str(root.val) + '->'
        self.get_path(root.left, path)
        self.get_path(root.right, path)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.path_list = []
        path = ""
        if root is None:
            return []
      
        self.get_path(root, path)
        return self.path_list


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root2 = TreeNode(1)
root3 = None

s = Solution()
print(s.binaryTreePaths(root))
print(s.binaryTreePaths(root2))
print(s.binaryTreePaths(root3))