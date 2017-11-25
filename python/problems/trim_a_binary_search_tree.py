"""
https://leetcode.com/problems/trim-a-binary-search-tree/description/

https://leetcode.com/submissions/detail/129562825/
"""

from common.tree_node import TreeNode
from common.assert_tree_node_equal import assertTreeNodeEqual

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def trimBST(self, root, L, R):
        """
        分成三种情况：
        - 判断 val
            - val 不在范围内
        - 判断 left
        - 判断 right

        此题二叉树符合左小右大的情况，因此：
        - val 过大时，取左子树
        - val 过小时，取右子树
        """
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree1.left = TreeNode(0)
        tree1.right = TreeNode(2)
        tree1output = TreeNode(1)
        tree1output.right = TreeNode(2)
        self.assertEqual(assertTreeNodeEqual(solution.trimBST(tree1, 1, 2), tree1output), True)


if __name__ == '__main__':
    unittest.main()
