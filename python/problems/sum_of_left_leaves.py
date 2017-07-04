"""
https://leetcode.com/problems/sum-of-left-leaves/

https://leetcode.com/submissions/detail/108272836/
"""

from common.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, sum, isLeft):
            if not node:
                return sum
            if isLeft and node.left == None and node.right == None:
                sum += node.val
                return sum
            sum = traverse(node.left, sum, True)
            sum = traverse(node.right, sum, False)
            return sum
        if root:
            return traverse(root, 0, False)
        return 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(3)
        treeNode1.left = TreeNode(9)
        treeNode1.right = TreeNode(20)
        treeNode1.right.left = TreeNode(15)
        treeNode1.right.right = TreeNode(7)
        self.assertEqual(solution.sumOfLeftLeaves(treeNode1), 24)

        treeNode2 = TreeNode(1)
        treeNode2.left = TreeNode(2)
        treeNode2.left.left = TreeNode(4)
        treeNode2.left.right = TreeNode(5)
        treeNode2.right = TreeNode(3)
        self.assertEqual(solution.sumOfLeftLeaves(treeNode2), 4)

if __name__ == '__main__':
    unittest.main()
