"""
https://leetcode.com/problems/complete-binary-tree-inserter/

https://leetcode.com/submissions/detail/185003747/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.tree_node import TreeNode
from common.list_to_tree_node import listToTreeNode
from common.tree_node_to_list import treeNodeToList

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.q = []

        queue = [root]
        while len(queue):
            node = queue[0]
            if not node.left or not node.right:
                self.q.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            queue.pop(0)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.q[0]
        self.q.append(TreeNode(v))
        if not node.left:
            node.left = self.q[-1]
        else:
            node.right = self.q[-1]
            self.q.pop(0)
        return node.val


    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()


import unittest


class Test(unittest.TestCase):
    def test(self):
        obj1 = CBTInserter(listToTreeNode([1]))
        self.assertEqual(obj1.insert(2), 1)
        self.assertEqual(treeNodeToList(obj1.get_root()), [1, 2])

        obj2 = CBTInserter(listToTreeNode([1, 2, 3, 4, 5, 6]))
        self.assertEqual(obj2.insert(7), 3)
        self.assertEqual(obj2.insert(8), 4)
        self.assertEqual(treeNodeToList(obj2.get_root()),
                         [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
