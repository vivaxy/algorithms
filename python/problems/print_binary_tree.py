"""
https://leetcode.com/problems/print-binary-tree/description/


"""

# from common.tree_node import TreeNode


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [['']]
        if not root.left and not root.right:
            return [[str(root.val)]]
        left = self.printTree(root.left)
        right = self.printTree(root.right)
        total = []

        # 补充缺少的行
        rowCount = max(len(left), len(right))
        if len(left) < rowCount:
            for rowIndex in range(rowCount - len(left)):
                left.append([''])
        if len(right) < rowCount:
            for rowIndex in range(rowCount - len(right)):
                right.append([''])
        for rowIndex in range(rowCount):
            leftPart = left[rowIndex]
            rightPart = right[rowIndex]
            # 补充缺少的列
            colCount = max(len(leftPart), len(rightPart))
            if len(left) < colCount:
                toMend = int((colCount - len(leftPart)) / 2)
                while toMend > 0:
                    leftPart = [''] + leftPart + ['']
                    toMend -= 1
            if len(rightPart) < colCount:
                toMend = int((colCount - len(rightPart)) / 2)
                while toMend > 0:
                    rightPart = [''] + rightPart + ['']
                    toMend -= 1
            total.append(leftPart + [''] + rightPart)
        firstRow = []
        for colIndex in range(len(total[0])):
            if int((len(total[0]) - 1) / 2) == colIndex:
                firstRow.append(str(root.val))
            else:
                firstRow.append('')
        return [firstRow] + total


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
