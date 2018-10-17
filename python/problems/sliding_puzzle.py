"""
https://leetcode.com/problems/sliding-puzzle/

https://leetcode.com/submissions/detail/138734643/
"""


class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        class Node(object):
            def __init__(self, state, depth):
                self.state = state
                self.depth = depth

        def move(inputB, diffCol, diffRow):
            b = []
            tileRow = None
            tileCol = None
            rowSize = len(inputB)
            colSize = len(inputB[0])
            for rowIndex in range(rowSize):
                newRow = []
                for colIndex in range(colSize):
                    num = inputB[rowIndex][colIndex]
                    if num == 0:
                        tileCol = colIndex
                        tileRow = rowIndex
                    newRow.append(num)
                b.append(newRow)
            if tileCol == None:
                return None
            if tileRow == None:
                return None
            nextTileRow = tileRow + diffRow
            nextTileCol = tileCol + diffCol
            if nextTileRow < 0:
                return None
            if nextTileRow >= rowSize:
                return None
            if nextTileCol < 0:
                return None
            if nextTileCol >= colSize:
                return None
            anotherNum = b[nextTileRow][nextTileCol]
            b[nextTileRow][nextTileCol] = 0
            b[tileRow][tileCol] = anotherNum
            return b

        states = []
        nodes = [Node(board, 0)]
        while len(nodes):
            node = nodes.pop(0)
            if not node:
                continue
            if node.state == [[1, 2, 3], [4, 5, 0]]:
                return node.depth
            if states.count(node.state) == 1:
                continue
            states.append(node.state)
            upNode = move(node.state, 0, -1)
            if upNode:
                nodes.append(Node(upNode, node.depth + 1))
            rightNode = move(node.state, 1, 0)
            if rightNode:
                nodes.append(Node(rightNode, node.depth + 1))
            downNode = move(node.state, 0, 1)
            if downNode:
                nodes.append(Node(downNode, node.depth + 1))
            leftNode = move(node.state, -1, 0)
            if leftNode:
                nodes.append(Node(leftNode, node.depth + 1))
        return -1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.slidingPuzzle([[1, 2, 3], [4, 0, 5]]), 1)
        self.assertEqual(solution.slidingPuzzle([[1, 2, 3], [5, 4, 0]]), -1)
        self.assertEqual(solution.slidingPuzzle([[4, 1, 2], [5, 0, 3]]), 5)
        self.assertEqual(solution.slidingPuzzle([[3, 2, 4], [1, 5, 0]]), 14)


if __name__ == '__main__':
    unittest.main()
