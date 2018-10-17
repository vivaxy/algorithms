"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

https://leetcode.com/submissions/detail/178517305/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.tree_node import TreeNode
from common.assert_tree_node_equal import assertTreeNodeEqual


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            root = TreeNode(val)
            return root
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
            return root
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
            return root
        return root


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        inTreeNode1 = TreeNode(4)
        inTreeNode1.left = TreeNode(2)
        inTreeNode1.right = TreeNode(7)
        inTreeNode1.left.left = TreeNode(1)
        inTreeNode1.left.right = TreeNode(3)
        outTreeNode1 = TreeNode(4)
        outTreeNode1.left = TreeNode(2)
        outTreeNode1.right = TreeNode(7)
        outTreeNode1.left.left = TreeNode(1)
        outTreeNode1.left.right = TreeNode(3)
        outTreeNode1.right.left = TreeNode(5)
        self.assertEqual(assertTreeNodeEqual(
            solution.insertIntoBST(inTreeNode1, 5), outTreeNode1), True)


if __name__ == '__main__':
    unittest.main()
