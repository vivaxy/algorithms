"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

https://leetcode.com/submissions/detail/148988804/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.tree_node import TreeNode


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(n, l):
            if n.left:
                dfs(n.left, l)
            l.append(n.val)
            if n.right:
                dfs(n.right, l)
            return l
        arr = dfs(root, [])
        return min([(j - i) for i, j in zip(arr, arr[1:])])


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(4)
        treeNode1.left = TreeNode(2)
        treeNode1.right = TreeNode(6)
        treeNode1.left.left = TreeNode(1)
        treeNode1.left.right = TreeNode(3)
        self.assertEqual(solution.minDiffInBST(treeNode1), 1)


if __name__ == '__main__':
    unittest.main()
