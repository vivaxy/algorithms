"""
https://leetcode.com/problems/surface-area-of-3d-shapes/

https://leetcode.com/submissions/detail/185200058/
"""


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for rowIndex in range(len(grid) + 1):
            for colIndex in range(len(grid[0]) + 1):
                if rowIndex >= len(grid):
                    prevRow = grid[rowIndex - 1]
                    if colIndex < len(prevRow):
                        ans += prevRow[colIndex]
                    continue

                if colIndex >= len(grid[rowIndex]):
                    if rowIndex < len(grid):
                        prevV = grid[rowIndex][colIndex - 1]
                        ans += prevV
                    continue

                v = grid[rowIndex][colIndex]
                if rowIndex == 0:
                    ans += v
                else:
                    prevV = grid[rowIndex - 1][colIndex]
                    ans += abs(v - prevV)
                if colIndex == 0:
                    ans += v
                elif colIndex >= len(grid[rowIndex]):
                    if rowIndex < len(grid):
                        prevV = grid[rowIndex][colIndex - 1]
                        ans += prevV
                    continue
                else:
                    prevV = grid[rowIndex][colIndex - 1]
                    ans += abs(v - prevV)
                if v > 0:
                    ans += 2
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.surfaceArea([[2]]), 10)
        self.assertEqual(solution.surfaceArea([[1, 2], [3, 4]]), 34)
        self.assertEqual(solution.surfaceArea([[1, 0], [0, 2]]), 16)
        self.assertEqual(solution.surfaceArea(
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 32)
        self.assertEqual(solution.surfaceArea(
            [[2, 2, 2], [2, 1, 2], [2, 2, 2]]), 46)


if __name__ == '__main__':
    unittest.main()
