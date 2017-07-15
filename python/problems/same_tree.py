"""
https://leetcode.com/problems/same-tree/

https://leetcode.com/submissions/detail/109733704/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.tree_node import TreeNode

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p:
            if q:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return False
        if q:
            return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        self.assertEqual(solution.isSameTree(treeNode1, treeNode2), False)


if __name__ == '__main':
    unittest.main()
