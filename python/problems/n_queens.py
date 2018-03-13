"""
https://leetcode.com/problems/n-queens/description/

https://leetcode.com/submissions/detail/144845461/
"""


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def buildBoard(size):
            board = []
            for rowIndex in range(size):
                row = []
                for colIndex in range(size):
                    row.append('.')
                board.append(row)
            return board

        def check(board, rowIndex, colIndex):
            # |
            for i in range(n):
                if board[i][colIndex] == 'Q':
                    return False
            # -
            for i in range(n):
                if board[rowIndex][i] == 'Q':
                    return False
            # / up
            r = rowIndex
            c = colIndex
            while c < n - 1 and r > 0:
                r -= 1
                c += 1
                if board[r][c] == 'Q':
                    return False
            # / down
            r = rowIndex
            c = colIndex
            while r < n - 1 and c > 0:
                r += 1
                c -= 1
                if board[r][c] == 'Q':
                    return False
            # \ down
            r = rowIndex
            c = colIndex
            while r < n - 1 and c < n - 1:
                r += 1
                c += 1
                if board[r][c] == 'Q':
                    return False
            # \ up
            r = rowIndex
            c = colIndex
            while r > 0 and c > 0:
                r -= 1
                c -= 1
                if board[r][c] == 'Q':
                    return False
            return True

        ans = []

        def traverse(pieces):
            lastPiece = pieces[len(pieces) - 1]
            nextRowIndex = lastPiece['rowIndex']
            nextColIndex = lastPiece['colIndex']
            board = buildBoard(n)
            for piece in pieces:
                if piece != lastPiece:
                    board[piece['rowIndex']][piece['colIndex']] = 'Q'
            if len(piece):
                if not check(board, nextRowIndex, nextColIndex):
                    return
            board[nextRowIndex][nextColIndex] = 'Q'
            if len(pieces) == n:
                ans.append(board)
                return
            while not (nextRowIndex == n - 1 and nextColIndex == n - 1):
                nextColIndex += 1
                if nextColIndex > n - 1:
                    nextColIndex = 0
                    nextRowIndex += 1
                traverse(
                    pieces + [{'rowIndex': nextRowIndex, 'colIndex': nextColIndex}])
        for rowIndex in range(n):
            for colIndex in range(n):
                traverse([{'rowIndex': rowIndex, 'colIndex': colIndex}])
        outAns = []
        for an in ans:
            outAn = []
            for row in an:
                outAn.append(''.join(row))
            outAns.append(outAn)
        return outAns


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.solveNQueens(4), [
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],
            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ])


if __name__ == '__main__':
    unittest.main()
