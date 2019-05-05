import unittest
"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

https://leetcode.com/submissions/detail/226913308/
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.v = 0
        def dfs(node: TreeNode) -> None:
            if node.right:
                dfs(node.right)
            self.v += node.val
            node.val = self.v
            if node.left:
                dfs(node.left)
        dfs(root)
        return root


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.bstToGst(listToTreeNode(
            [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
        ))), [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8])


if __name__ == '__main__':
    unittest.main()
