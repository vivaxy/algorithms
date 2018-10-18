"""
https://leetcode.com/problems/increasing-order-search-tree/

https://leetcode.com/submissions/detail/183592991/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.tree_node import TreeNode
from common.list_to_tree_node import listToTreeNode
from common.tree_node_to_list import treeNodeToList


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = TreeNode(None)
        self.parent = ans

        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.parent.right = node
                self.parent = node
                inorder(node.right)
        inorder(root)
        return ans.right


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.increasingBST(
            listToTreeNode([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
        )), treeNodeToList(listToTreeNode([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])))


if __name__ == '__main__':
    unittest.main()
