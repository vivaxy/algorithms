"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


"""

from typing import List
from common.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        ans = None
        if len(preorder):
            ans = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                ans.left = self.bstFromPreorder(preorder[1:i])
                ans.right = self.bstFromPreorder(preorder[i:])
            break
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.bstFromPreorder([]), [])


if __name__ == '__main__':
    unittest.main()
