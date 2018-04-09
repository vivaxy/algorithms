"""
https://leetcode.com/problems/binary-tree-pruning/description/

https://leetcode.com/submissions/detail/149147905/
"""

from common.tree_node import TreeNode
from common.assert_tree_node_equal import assertTreeNodeEqual

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        if root and root.val == 0 and root.left == None and root.right == None:
            root = None
        return root


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(1)
        treeNode1.right = TreeNode(0)
        treeNode1.right.left = TreeNode(0)
        treeNode1.right.right = TreeNode(1)
        treeNode11 = TreeNode(1)
        treeNode11.right = TreeNode(0)
        treeNode11.right.right = TreeNode(1)
        self.assertEqual(assertTreeNodeEqual(
            solution.pruneTree(treeNode1), treeNode11), True)


if __name__ == '__main__':
    unittest.main()
