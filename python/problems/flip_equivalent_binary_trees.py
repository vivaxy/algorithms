"""
https://leetcode.com/problems/flip-equivalent-binary-trees/

https://leetcode.com/submissions/detail/216375860/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.tree_node import TreeNode
from common.list_to_tree_node import listToTreeNode


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
                return True
            if self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
                return True
        return False



import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.flipEquiv(
            listToTreeNode([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
            listToTreeNode([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]),
        ), True)


if __name__ == '__main__':
    unittest.main()
