"""
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

https://leetcode.com/submissions/detail/179391559/
"""

from common.n_ary_tree_node import Node


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            if len(root.children):
                return 1 + max(map(lambda child: self.maxDepth(child), root.children))
            return 1
        return 0


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        rootNode1 = Node(
            1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
        self.assertEqual(solution.maxDepth(rootNode1), 3)


if __name__ == '__main__':
    unittest.main()
