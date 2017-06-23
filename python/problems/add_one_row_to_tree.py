"""
https://leetcode.com/problems/add-one-row-to-tree/

https://leetcode.com/submissions/detail/107013179/
"""

from common.tree_node import TreeNode


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            treeNode = TreeNode(v)
            treeNode.left = root
            return treeNode
        elif d == 2:
            left = root.left
            right = root.right
            root.left = TreeNode(v)
            root.right = TreeNode(v)
            root.left.left = left
            root.right.right = right
            return root
        else:
            if root.left:
                self.addOneRow(root.left, v, d - 1)
            if root.right:
                self.addOneRow(root.right, v, d - 1)
            return root


import unittest
from common.assert_tree_node_equal import assertTreeNodeEqual


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right = TreeNode(6)
        root.right.left = TreeNode(5)
        newRoot = TreeNode(4)
        newRoot.left = TreeNode(1)
        newRoot.left.left = TreeNode(2)
        newRoot.left.left.left = TreeNode(3)
        newRoot.left.left.right = TreeNode(1)
        newRoot.right = TreeNode(1)
        newRoot.right.right = TreeNode(6)
        newRoot.right.right.left = TreeNode(5)
        self.assertTrue(assertTreeNodeEqual(
            solution.addOneRow(root, 1, 2), newRoot))


if __name__ == '__main__':
    unittest.main()
