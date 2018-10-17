"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

https://leetcode.com/submissions/detail/146961062/
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        topBottomSkyline = [0] * len(grid[0])
        leftRightSkyline = [0] * len(grid)
        for rowIndex in range(len(grid)):
            row = grid[rowIndex]
            for colIndex in range(len(row)):
                if topBottomSkyline[colIndex] < row[colIndex]:
                    topBottomSkyline[colIndex] = row[colIndex]
                if leftRightSkyline[rowIndex] < row[colIndex]:
                    leftRightSkyline[rowIndex] = row[colIndex]
        ans = 0
        for rowIndex in range(len(grid)):
            row = grid[rowIndex]
            for colIndex in range(len(row)):
                ans += min(leftRightSkyline[rowIndex],
                           topBottomSkyline[colIndex]) - row[colIndex]
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxIncreaseKeepingSkyline(
            [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]), 35)


if __name__ == '__main__':
    unittest.main()
