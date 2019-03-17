"""
https://leetcode.com/problems/univalued-binary-tree/

https://leetcode.com/submissions/detail/215467422/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.tree_node import TreeNode
from common.list_to_tree_node import listToTreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            if root.left and root.right:
                return root.val == root.left.val and root.val == root.right.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            if root.left:
                return root.val == root.left.val and self.isUnivalTree(root.left)
            if root.right:
                return root.val == root.right.val and self.isUnivalTree(root.right)
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.isUnivalTree(listToTreeNode(
            [1, 1, 1, 1, 1, None, 1]
        )), True)
        self.assertEqual(solution.isUnivalTree(listToTreeNode(
            [2, 2, 2, 5, 2]
        )), False)


if __name__ == '__main__':
    unittest.main()
