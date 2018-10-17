"""
https://leetcode.com/problems/max-area-of-island/

https://leetcode.com/submissions/detail/139333744/
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        seen = set()
        rowCount = len(grid)
        colCount = len(grid[0])

        def getArea(rowIndex, colIndex):
            if rowIndex < 0:
                return 0
            if colIndex < 0:
                return 0
            if rowIndex >= rowCount:
                return 0
            if colIndex >= colCount:
                return 0
            if (rowIndex, colIndex) in seen:
                return 0
            if grid[rowIndex][colIndex] == 0:
                return 0
            seen.add((rowIndex, colIndex))
            return 1 + getArea(rowIndex, colIndex + 1) + getArea(rowIndex, colIndex - 1) + getArea(rowIndex + 1, colIndex) + getArea(rowIndex - 1, colIndex)

        for rowIndex in range(rowCount):
            for colIndex in range(colCount):
                currentArea = getArea(rowIndex, colIndex)
                if currentArea > maxArea:
                    maxArea = currentArea
        return maxArea


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxAreaOfIsland([
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]), 6)
        self.assertEqual(solution.maxAreaOfIsland([
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]), 0)


if __name__ == '__main__':
    unittest.main()
