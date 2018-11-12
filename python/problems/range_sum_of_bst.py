"""
https://leetcode.com/problems/range-sum-of-bst/

https://leetcode.com/submissions/detail/189028356/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.list_to_tree_node import listToTreeNode


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        left, right = 0, 0
        if root.left:
            left = self.rangeSumBST(root.left, L, R)
        if root.right:
            right = self.rangeSumBST(root.right, L, R)
        if root.val >= L and root.val <= R:
            return left + right + root.val
        return left + right


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.rangeSumBST(
            listToTreeNode([10, 5, 15, 3, 7, None, 18]), 7, 15), 32)
        self.assertEqual(solution.rangeSumBST(listToTreeNode(
            [10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10), 23)


if __name__ == '__main__':
    unittest.main()
