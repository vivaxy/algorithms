"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

https://leetcode.com/submissions/detail/184669956/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.tree_node import TreeNode
from common.tree_node_to_list import treeNodeToList


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(treeNodeToList(solution.constructFromPrePost(
            [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])), [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
