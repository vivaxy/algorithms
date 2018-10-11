"""
https://leetcode.com/problems/leaf-similar-trees/description/

https://leetcode.com/submissions/detail/181931434/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.list_to_tree_node import listToTreeNode


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaf(root):
            ans = []

            def traverse(node):
                if not node.left and not node.right:
                    ans.append(node.val)
                else:
                    if node.left:
                        traverse(node.left)
                    if node.right:
                        traverse(node.right)
            traverse(root)
            return ans
        return getLeaf(root1) == getLeaf(root2)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.leafSimilar(
            listToTreeNode([3,
                            5, 1,
                            6, 2, 9, 8,
                            None, None, 7, 4]),
            listToTreeNode([1,
                            2, 3,
                            6, 4, 9, 8,
                            None, None, 7, 4])
        ), True)
        self.assertEqual(solution.leafSimilar(
            listToTreeNode([1]), listToTreeNode([2])), False)


if __name__ == '__main__':
    unittest.main()
