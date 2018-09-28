"""
https://leetcode.com/problems/search-in-a-binary-search-tree/description/

https://leetcode.com/submissions/detail/179015002/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.list_to_tree_node import listToTreeNode
from common.tree_node_to_list import treeNodeToList


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.searchBST(
            listToTreeNode([4, 2, 7, 1, 3]), 2)), [2, 1, 3])


if __name__ == '__main__':
    unittest.main()
