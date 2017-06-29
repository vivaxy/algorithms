"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

https://leetcode.com/submissions/detail/107716797/
"""


from common.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, l=[]):
            if node.left:
                dfs(node.left, l)
            l.append(node.val)
            if node.right:
                dfs(node.right, l)
            return l
        l = dfs(root)
        return min([abs(a - b) for a, b in zip(l, l[1:])])


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()

        treeNode1 = TreeNode(1)
        treeNode1.right = TreeNode(3)
        treeNode1.right.left = TreeNode(2)
        self.assertEqual(solution.getMinimumDifference(treeNode1), 1)


if __name__ == '__main__':
    unittest.main()
