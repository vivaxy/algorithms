"""
https://leetcode.com/problems/print-binary-tree/description/

https://leetcode.com/submissions/detail/132220547/
"""

from common.tree_node import TreeNode


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        """
        1. 广度优先遍历树节点
        2. 从最后一层开始拼树组
        """
        totalBfsList = []
        previousBfsList = [root]
        nextBfsList = []
        nextAllNone = False
        while not nextAllNone:
            previousBfsValList = []
            for node in previousBfsList:
                if not node:
                    nextBfsList.append(None)
                    nextBfsList.append(None)
                    previousBfsValList.append(None)
                else:
                    nextBfsList.append(node.left)
                    nextBfsList.append(node.right)
                    previousBfsValList.append(node.val)
            totalBfsList.append(previousBfsValList)
            previousBfsList = []
            nextAllNone = True
            for node in nextBfsList:
                if node:
                    nextAllNone = False
                previousBfsList.append(node)
            nextBfsList = []
        gap = 0
        result = []
        while len(totalBfsList):
            currentList = totalBfsList.pop()
            row = []
            for val in currentList:
                if val == None:
                    val = ''
                row = row + [''] * gap + [str(val)] + [''] * gap + ['']
            row.pop()
            gap = gap * 2 + 1
            result = [row] + result
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        treeNode1 = TreeNode(1)
        treeNode1.left = TreeNode(2)
        self.assertEqual(solution.printTree(treeNode1), [
            ["", "1", ""],
            ["2", "", ""]
        ])
        treeNode2 = TreeNode(1)
        treeNode2.left = TreeNode(2)
        treeNode2.right = TreeNode(3)
        treeNode2.left.right = TreeNode(4)
        self.assertEqual(solution.printTree(treeNode2), [
            ["", "", "", "1", "", "", ""],
            ["", "2", "", "", "", "3", ""],
            ["", "", "4", "", "", "", ""]
        ])
        treeNode3 = TreeNode(1)
        treeNode3.left = TreeNode(2)
        treeNode3.left.left = TreeNode(3)
        treeNode3.left.left.left = TreeNode(4)
        treeNode3.right = TreeNode(5)
        self.assertEqual(solution.printTree(treeNode3), [
            ["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
            ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""],
            ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
            ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
        ])
        treeNode4 = TreeNode(3)
        treeNode4.left = TreeNode(1)
        treeNode4.left.left = TreeNode(0)
        treeNode4.left.right = TreeNode(2)
        treeNode4.left.right.right = TreeNode(3)
        treeNode4.right = TreeNode(5)
        treeNode4.right.left = TreeNode(4)
        treeNode4.right.right = TreeNode(6)
        self.assertEqual(solution.printTree(treeNode4), [
            ["",  "", "",  "", "",  "",  "", "3", "",  "", "",  "", "",  "", ""],
            ["",  "", "", "1", "",  "",  "",  "", "",  "", "", "5", "",  "", ""],
            ["", "0", "",  "", "", "2",  "",  "", "", "4", "",  "", "", "6", ""],
            ["",  "", "",  "", "",  "", "3",  "", "",  "", "",  "", "",  "", ""]
        ])


if __name__ == '__main__':
    unittest.main()
