"""
https://leetcode.com/problems/all-possible-full-binary-trees/

https://leetcode.com/submissions/detail/177298207/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.tree_node import TreeNode
from common.tree_node_to_list import treeNodeToList


class Solution:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        ans.append(node)
            Solution.memo[N] = ans
        return Solution.memo[N]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(list(map(lambda x: treeNodeToList(x), solution.allPossibleFBT(7))), [
            [0, 0, 0, None, None, 0, 0, None, None, 0, 0],
            [0, 0, 0, None, None, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
            [0, 0, 0, 0, 0, None, None, 0, 0]
        ])


if __name__ == '__main__':
    unittest.main()
