"""
https://leetcode.com/problems/minesweeper/

https://leetcode.com/submissions/detail/106907707/
"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i = click[0]
        j = click[1]
        iLen = len(board)
        jLen = len(board[0])
        cell = board[i][j]
        if cell == 'M':
            board[i][j] = 'X'
        elif cell == 'E':
            self.revealRecursively(board, iLen, jLen, i, j)
        return board

    def revealRecursively(self, board, iLen, jLen, i, j):
        cell = board[i][j]
        if cell != 'E':
            return
        mines, emptyCells = self.getAdjacentCells(board, iLen, jLen, i, j)
        if mines == 0:
            board[i][j] = 'B'
            self.revealRecursively(board, iLen, jLen, i, j)
            for pos in emptyCells:
                self.revealRecursively(board, iLen, jLen, pos[0], pos[1])
        else:
            board[i][j] = str(mines)

    def getAdjacentCells(self, board, iLen, jLen, i, j):
        if i < 0 or j < 0 or i > iLen or j > jLen:
            return None, None
        mines = 0
        emptyCells = []
        cells = [
            [i - 1, j - 1],
            [i - 1, j],
            [i - 1, j + 1],
            [i, j - 1],
            [i, j + 1],
            [i + 1, j - 1],
            [i + 1, j],
            [i + 1, j + 1],
        ]
        for cell in cells:
            cur = self.getCell(board, iLen, jLen, cell[0], cell[1])
            if cur == 'M':
                mines += 1
            if cur == 'E':
                emptyCells.append(cell)
        return mines, emptyCells

    def getCell(self, board, iLen, jLen, i, j):
        if i < 0 or j < 0 or i >= iLen or j >= jLen:
            return None
        return board[i][j]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        board1 = [
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'M', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E']
        ]
        output1 = [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']
        ]
        self.assertEqual(solution.updateBoard(board1, [3, 0]), output1)

        board2 = [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']
        ]
        output2 = [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'X', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']
        ]
        self.assertEqual(solution.updateBoard(board2, [1, 2]), output2)


if __name__ == '__main__':
    unittest.main()
