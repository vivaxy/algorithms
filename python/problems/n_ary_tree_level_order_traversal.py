"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

https://leetcode.com/submissions/detail/184433348/
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from common.n_ary_tree_node import Node


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []

        def traverse(node, depth):
            if not node:
                return
            if len(ans) < depth:
                ans.append([])
            ans[depth - 1].append(node.val)
            for child in node.children:
                traverse(child, depth + 1)
        traverse(root, 1)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        rootNode1 = Node(1, [
            Node(3, [
                Node(5, []),
                Node(6, [])
            ]),
            Node(2, []),
            Node(4, [])
        ])
        self.assertEqual(solution.levelOrder(rootNode1), [
            [1],
            [3, 2, 4],
            [5, 6]
        ])


if __name__ == '__main__':
    unittest.main()
