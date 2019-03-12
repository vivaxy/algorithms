import unittest
"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

https://leetcode.com/submissions/detail/214138493/
"""

from typing import List
from common.tree_node import TreeNode
from common.tree_node_to_list import treeNodeToList

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        ans = TreeNode(preorder[0])
        idx = 1
        for i in range(1, len(preorder)):
            idx = i
            if preorder[i] > preorder[0]:
                break
        if preorder[idx] < preorder[0]:
            idx += 1
        ans.left = self.bstFromPreorder(preorder[1:idx])
        ans.right = self.bstFromPreorder(preorder[idx:])
        return ans


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.bstFromPreorder(
            [8, 5, 1, 7, 10, 12])), [8, 5, 10, 1, 7, None, 12])
        self.assertEqual(treeNodeToList(
            solution.bstFromPreorder([4, 2])), [4, 2])


if __name__ == '__main__':
    unittest.main()
