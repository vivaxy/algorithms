"""
https://leetcode.com/problems/maximum-binary-tree/

https://leetcode.com/submissions/detail/117135480/
"""

from common.tree_node import TreeNode
from common.print_tree_node import printTreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        rootTreeNode = None
        for num in nums:
            if rootTreeNode == None:
                rootTreeNode = TreeNode(num)
                currentTreeNode = rootTreeNode
            else:
                parentTreeNode = None
                currentTreeNode = rootTreeNode
                while currentTreeNode != None:
                    if num > currentTreeNode.val:
                        if parentTreeNode == None:
                            newTreeNode = TreeNode(num)
                            newTreeNode.left = rootTreeNode
                            rootTreeNode = newTreeNode
                        else:
                            parentTreeNode.right = TreeNode(num)
                            parentTreeNode.right.left = currentTreeNode
                        break
                    else:
                        parentTreeNode = currentTreeNode
                        currentTreeNode = currentTreeNode.right
                if currentTreeNode == None:
                    parentTreeNode.right = TreeNode(num)
        return rootTreeNode


import unittest
from common.assert_tree_node_equal import assertTreeNodeEqual


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        rootTreeNode1 = TreeNode(6)
        rootTreeNode1.left = TreeNode(3)
        rootTreeNode1.left.right = TreeNode(2)
        rootTreeNode1.left.right.right = TreeNode(1)
        rootTreeNode1.right = TreeNode(5)
        rootTreeNode1.right.left = TreeNode(0)
        self.assertTrue(assertTreeNodeEqual(
            solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]), rootTreeNode1))


if __name__ == '__main__':
    unittest.main()
