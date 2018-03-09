"""
https://leetcode.com/problems/n-queens/description/


"""


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def buildBoard(size):
            return ['.' * size] * size

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
            while c < n and r >= 0:
                r -= 1
                c += 1
                if board[r][c] == 'Q':
                    return False
            # / down
            r = rowIndex
            c = colIndex
            while r < n and c >= 0:
                r += 1
                c -= 1
                if board[r][c] == 'Q':
                    return False
            # \ up
            r = rowIndex
            c = colIndex
            while r < n and c < n:
                r += 1
                c += 1
                if board[r][c] == 'Q':
                    return False
            # \ down
            r = rowIndex
            c = colIndex
            while r >= 0 and c >= 0:
                r -= 1
                c -= 1
                if board[r][c] == 'Q':
                    return False
            return True

        def traverse():
            pass


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
