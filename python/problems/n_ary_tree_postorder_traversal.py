"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/

https://leetcode.com/submissions/detail/179182067/
"""


from common.n_ary_tree_node import Node


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        ans = []
        for child in root.children:
            ans = ans + self.postorder(child)
        return ans + [root.val]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        rootNode1 = Node(1, [])
        rootNode1.children.append(Node(3, []))
        rootNode1.children.append(Node(2, []))
        rootNode1.children.append(Node(4, []))
        rootNode1.children[0].children.append(Node(5, []))
        rootNode1.children[0].children.append(Node(6, []))
        self.assertEqual(solution.postorder(rootNode1), [5, 6, 3, 2, 4, 1])


if __name__ == '__main__':
    unittest.main()
