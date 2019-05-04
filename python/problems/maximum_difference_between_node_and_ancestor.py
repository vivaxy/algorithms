"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

https://leetcode.com/submissions/detail/226688002/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.list_to_tree_node import listToTreeNode
from common.tree_node import TreeNode


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0
        ways = [[root, root.val, root.val]]
        while len(ways):
            node, _min, _max = ways.pop(0)
            if node.val > _max:
                _max = node.val
            if node.val < _min:
                _min = node.val

            if node.left:
                ways.append([node.left, _min, _max])
            if node.right:
                ways.append([node.right, _min, _max])
            ans = max(_max - _min, ans)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxAncestorDiff(listToTreeNode(
            [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
        )), 7)
        self.assertEqual(solution.maxAncestorDiff(listToTreeNode(
            [2, None, 0, 1]
        )), 2)


if __name__ == '__main__':
    unittest.main()
