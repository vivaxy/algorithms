"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

https://leetcode.com/submissions/detail/141037270/
"""

from common.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(1)
        treeNode1.right = TreeNode(2)
        treeNode1.right.left = TreeNode(3)
        self.assertEqual(solution.inorderTraversal(treeNode1), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
