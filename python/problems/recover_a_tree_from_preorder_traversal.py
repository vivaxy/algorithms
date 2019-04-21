"""
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

https://leetcode.com/submissions/detail/223923297/
https://leetcode.com/submissions/detail/223925605/
"""

from common.tree_node import TreeNode
from common.tree_node_to_list import treeNodeToList
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0

        def pollNode(i: int) -> (int, int, int):
            depth, val = 0, ''
            while i < len(S):
                char = S[i]
                if val != '':
                    if char == '-':
                        break
                    val += char
                    i += 1
                    continue
                if char == '-':
                    depth += 1
                    i += 1
                    continue
                val += char
                i += 1
            return depth + 1, int(val), i
        depth, val, i = pollNode(i)
        root = TreeNode(val)
        parents = [root]

        def setTreeNode(depth: int, val: int) -> None:
            if depth > len(parents) + 1:
                raise BaseException('Unexpected Depth')
            key = 'left'
            if depth <= len(parents):
                key = 'right'
                while depth <= len(parents):
                    parents.pop()
            newTreeNode = TreeNode(val)
            if key == 'left':
                parents[len(parents) - 1].left = newTreeNode
            else:
                parents[len(parents) - 1].right = newTreeNode
            parents.append(newTreeNode)
        while i < len(S) - 1:
            depth, val, i = pollNode(i)
            setTreeNode(depth, val)
        return root


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.recoverFromPreorder(
            "1-2--3--4-5--6--7"
        )), [1, 2, 5, 3, 4, 6, 7])
        self.assertEqual(treeNodeToList(solution.recoverFromPreorder(
            "1-2--3---4-5--6---7"
        )), [1, 2, 5, 3, None, 6, None, 4, None, 7])
        self.assertEqual(treeNodeToList(solution.recoverFromPreorder(
            "1-401--349---90--88"
        )), [1, 401, None, 349, 88, 90])
        self.assertEqual(treeNodeToList(solution.recoverFromPreorder(
            "3"
        )), [3])
        self.assertEqual(treeNodeToList(solution.recoverFromPreorder(
            "10-7--8"
        )), [10, 7, None, 8])


if __name__ == '__main__':
    unittest.main()
