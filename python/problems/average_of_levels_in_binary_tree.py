"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/

https://leetcode.com/submissions/detail/109018600/
"""


from common.tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def traverse(nodes, array):
            if len(nodes) == 0:
                return array
            nextNodes = []
            values = []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            array.append(sum(values) / len(values))
            return traverse(nextNodes, array)
        return traverse([root], [])


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(3)
        treeNode1.left = TreeNode(9)
        treeNode1.right = TreeNode(20)
        treeNode1.right.left = TreeNode(15)
        treeNode1.right.right = TreeNode(7)
        self.assertEqual(solution.averageOfLevels(treeNode1), [3, 14.5, 11])


if __name__ == '__main__':
    unittest.main()
