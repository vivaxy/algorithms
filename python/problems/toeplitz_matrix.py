"""
https://leetcode.com/problems/toeplitz-matrix/

https://leetcode.com/submissions/detail/137278039/
"""


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rowCount = len(matrix)
        colCount = len(matrix[0])
        for rowIndex in range(rowCount):
            col = 0
            row = rowIndex
            num = matrix[row][col]
            col += 1
            row += 1
            while row < rowCount and col < colCount:
                number = matrix[row][col]
                if num != number:
                    return False
                col += 1
                row += 1
        for colIndex in range(1, colCount):
            col = colIndex
            row = 0
            num = matrix[row][col]
            col += 1
            row += 1
            while row < rowCount and col < colCount:
                number = matrix[row][col]
                if num != number:
                    return False
                col += 1
                row += 1
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        # self.assertEqual(solution.isToeplitzMatrix(
        #     [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
        self.assertEqual(solution.isToeplitzMatrix([[1, 2], [2, 2]]), False)


if __name__ == '__main__':
    unittest.main()
