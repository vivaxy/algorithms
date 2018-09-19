"""
https://leetcode.com/problems/score-after-flipping-matrix/description/

https://leetcode.com/submissions/detail/176979117/
"""


class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        score = 0
        rowCount = len(A)
        colCount = len(A[0])
        needMoveRow = []
        for colIndex in range(colCount):
            colScore = 0
            for rowIndex in range(rowCount):
                if colIndex == 0:
                    needMoveRow.append(A[rowIndex][colIndex] == 0)
                if needMoveRow[rowIndex]:
                    colScore += 1 - A[rowIndex][colIndex]
                else:
                    colScore += A[rowIndex][colIndex]
            if rowCount - colScore > colScore:
                colScore = rowCount - colScore
            score += colScore * 2 ** (colCount - colIndex - 1)
        return score


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.matrixScore(
            [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]), 39)


if __name__ == '__main__':
    unittest.main()
