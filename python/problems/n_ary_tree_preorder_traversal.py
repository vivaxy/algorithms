"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

https://leetcode.com/submissions/detail/180540212/
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if len(root.children):
            ans = [root.val]
            for arr in map(lambda child: self.preorder(child), root.children):
                ans += arr
            return ans
        return [root.val]


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
        self.assertEqual(solution.preorder(rootNode1), [1, 3, 5, 6, 2, 4])


if __name__ == '__main__':
    unittest.main()
