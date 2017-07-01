"""
https://leetcode.com/problems/binary-tree-tilt/

https://leetcode.com/submissions/detail/107929547/
"""

from common.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, tilt):
            if node == None:
                return 0, 0
            valLeft, tiltLeft = traverse(node.left, tilt)
            valRight, tiltRight = traverse(node.right, tilt)
            return (node.val + valLeft + valRight), (tilt + abs(valLeft - valRight) + tiltLeft + tiltRight)
        val, tilt = traverse(root, 0)
        return tilt


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(1)
        treeNode1.left = TreeNode(2)
        treeNode1.right = TreeNode(3)
        self.assertEqual(solution.findTilt(treeNode1), 1)


if __name__ == '__main__':
    unittest.main()
