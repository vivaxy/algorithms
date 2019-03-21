"""
https://leetcode.com/problems/maximum-binary-tree-ii/

https://leetcode.com/submissions/detail/216622437/
"""

from common.tree_node import TreeNode
from common.list_to_tree_node import listToTreeNode
from common.tree_node_to_list import treeNodeToList

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            raise 'root is not defined'
        if val >= root.val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        if root.right:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        root.right = TreeNode(val)
        return root

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root and val < root.val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        newRoot = TreeNode(val)
        newRoot.left = root
        return newRoot


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.insertIntoMaxTree(listToTreeNode(
            [4, 1, 3, None, None, 2]), 5
        )), [5, 4, None, 1, 3, None, None, 2])
        self.assertEqual(treeNodeToList(solution.insertIntoMaxTree(listToTreeNode(
            [5, 2, 4, None, 1]), 3
        )), [5, 2, 4, None, 1, None, 3])
        self.assertEqual(treeNodeToList(solution.insertIntoMaxTree(listToTreeNode(
            [5, 2, 3, None, 1]), 4
        )), [5, 2, 4, None, 1, 3])


if __name__ == '__main__':
    unittest.main()
