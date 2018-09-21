"""
https://leetcode.com/problems/projection-area-of-3d-shapes/description/

https://leetcode.com/submissions/detail/177472226/
"""


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        maxInCol = []
        for rowIndex in range(len(grid)):
            row = grid[rowIndex]
            maxInRow = 0
            for colIndex in range(len(row)):
                item = row[colIndex]
                maxInRow = max(maxInRow, item)
                if item > 0:
                    ans += 1
                if rowIndex == 0:
                    maxInCol.append(item)
                else:
                    maxInCol[colIndex] = max(maxInCol[colIndex], item)
                if rowIndex == len(grid) - 1:
                    ans += maxInCol[colIndex]
            ans += maxInRow
        return ans

import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.projectionArea([[2]]), 5)
        self.assertEqual(solution.projectionArea([[1, 2], [3, 4]]), 17)
        self.assertEqual(solution.projectionArea([[1, 0], [0, 2]]), 8)
        self.assertEqual(solution.projectionArea(
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 14)
        self.assertEqual(solution.projectionArea(
            [[2, 2, 2], [2, 1, 2], [2, 2, 2]]), 21)


if __name__ == '__main__':
    unittest.main()
