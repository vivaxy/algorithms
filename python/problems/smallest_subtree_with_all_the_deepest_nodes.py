"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.list_to_tree_node import listToTreeNode
from common.tree_node_to_list import treeNodeToList


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while len(stack) > 1 or (stack[0].left and (stack[0].left.left or stack[0].left.right)) or (stack[0].right and (stack[0].right.left or stack[0].right.right)):
            node = stack.pop(0)
            if node.left and (node.left.left or node.left.right):
                stack.append(node.left)
            if node.right and (node.right.left or node.right.right):
                stack.append(node.right)
        return stack[0]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.subtreeWithAllDeepest(
            listToTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        )), [2, 7, 4])
        self.assertEqual(treeNodeToList(solution.subtreeWithAllDeepest(
            listToTreeNode([0, 2, 1, None, None, 3])
        )), [1, 3])
        # self.assertEqual(treeNodeToList(solution.subtreeWithAllDeepest(
        #     listToTreeNode([0, 1, 3, None, 2])
        # )), [2])


if __name__ == '__main__':
    unittest.main()
