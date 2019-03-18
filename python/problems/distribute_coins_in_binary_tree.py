"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/

https://leetcode.com/submissions/detail/215845361/
"""

from common.tree_node import TreeNode
from common.list_to_tree_node import listToTreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            moveLeft = dfs(node.left)
            moveRight = dfs(node.right)
            self.ans += abs(moveLeft) + abs(moveRight)
            return node.val + moveLeft + moveRight - 1

        dfs(root)

        return self.ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.distributeCoins(listToTreeNode(
            [3, 0, 0]
        )), 2)
        self.assertEqual(solution.distributeCoins(listToTreeNode(
            [0, 3, 0]
        )), 3)
        self.assertEqual(solution.distributeCoins(listToTreeNode(
            [1, 0, 2]
        )), 2)
        self.assertEqual(solution.distributeCoins(listToTreeNode(
            [1, 0, 0, None, 3]
        )), 4)


if __name__ == '__main__':
    unittest.main()
