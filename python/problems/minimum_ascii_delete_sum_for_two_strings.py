"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

https://leetcode.com/submissions/detail/136983639/
"""


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        matrix = []
        firstRows = list(map(ord, s1))
        firstCols = list(map(ord, s2))
        for rowIndex, col in enumerate(firstCols):
            matrixRow = []
            for colIndex, row in enumerate(firstRows):
                if rowIndex == 0:
                    if colIndex == 0:
                        if row == col:
                            matrixRow.append(0)
                        else:
                            matrixRow.append(row + col)
                    else:
                        if row == col:
                            # 使用左上角的值（累加）
                            matrixRow.append(sum(firstRows[:colIndex]))
                        else:
                            matrixRow.append(matrixRow[colIndex - 1] + row)
                else:
                    if colIndex == 0:
                        if row == col:
                            # 使用左上角的值（累加）
                            matrixRow.append(sum(firstCols[:rowIndex]))
                        else:
                            matrixRow.append(matrix[rowIndex - 1][colIndex] + col)
                    else:
                        if row == col:
                            matrixRow.append(matrix[rowIndex - 1][colIndex - 1])
                        else:
                            topWithCol = matrix[rowIndex - 1][colIndex] + col
                            leftWithRow = matrixRow[colIndex - 1] + row
                            if topWithCol > leftWithRow:
                                matrixRow.append(leftWithRow)
                            else:
                                matrixRow.append(topWithCol)
            matrix.append(matrixRow)
        return matrix.pop().pop()


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minimumDeleteSum('sea', 'eat'), 231)
        self.assertEqual(solution.minimumDeleteSum('delete', 'leet'), 403)
        self.assertEqual(solution.minimumDeleteSum('a', 'at'), 116)


if __name__ == '__main__':
    unittest.main()
