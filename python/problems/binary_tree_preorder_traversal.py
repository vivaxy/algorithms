"""
https://leetcode.com/problems/binary-tree-preorder-traversal/description/


"""

from common.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        arr = [root]
        while len(arr):
            node = arr[0]
            arr.remove(node)
            if node:
                ans.append(node.val)
                if node.right:
                    arr.insert(0, node.right)
                if node.left:
                    arr.insert(0, node.left)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(1)
        treeNode1.right = TreeNode(2)
        treeNode1.right.left = TreeNode(3)
        self.assertEqual(solution.preorderTraversal(treeNode1), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
