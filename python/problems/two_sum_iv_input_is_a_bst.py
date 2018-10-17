"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

https://leetcode.com/submissions/detail/130583255/
"""

from common.tree_node import TreeNode


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False

        def dfs(node, value):
            if value == k / 2:
                return False
            if node == None:
                return False
            if value == node.val:
                return True
            if value < node.val:
                return dfs(node.left, value)
            if value > node.val:
                return dfs(node.right, value)

        def traverse(node):
            if node == None:
                return False
            return dfs(root, k - node.val) or traverse(node.left) or traverse(node.right)
        return traverse(root)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()

        treeNode1 = TreeNode(5)
        treeNode1.left = TreeNode(3)
        treeNode1.left.left = TreeNode(2)
        treeNode1.left.right = TreeNode(4)
        treeNode1.right = TreeNode(6)
        treeNode1.right.right = TreeNode(7)
        self.assertEqual(solution.findTarget(treeNode1, 9), True)

        treeNode2 = TreeNode(5)
        treeNode2.left = TreeNode(3)
        treeNode2.left.left = TreeNode(2)
        treeNode2.left.right = TreeNode(4)
        treeNode2.right = TreeNode(6)
        treeNode2.right.right = TreeNode(7)
        self.assertEqual(solution.findTarget(treeNode2, 28), False)

        treeNode3 = TreeNode(2)
        treeNode3.left = TreeNode(1)
        treeNode3.right = TreeNode(3)
        self.assertEqual(solution.findTarget(treeNode3, 4), True)

        treeNode4 = TreeNode(1)
        self.assertEqual(solution.findTarget(treeNode4, 2), False)

        treeNode5 = TreeNode(0)
        treeNode5.left = TreeNode(-1)
        treeNode5.left.left = TreeNode(-3)
        treeNode5.right = TreeNode(2)
        treeNode5.right.right = TreeNode(4)
        self.assertEqual(solution.findTarget(treeNode5, -4), True)


if __name__ == '__main__':
    unittest.main()
