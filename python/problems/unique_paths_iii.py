"""
https://leetcode.com/problems/unique-paths-iii/

https://leetcode.com/submissions/detail/213658070/
"""

from typing import List


class Solution:
    """
    1. find start point
    2. find all possible next start points
        1. update grid
        2. recursively call self
    3. ans += 1
    """

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        rowCount = len(grid)
        colCount = len(grid[0])

        def findStartPoint(g):
            for ri in range(len(g)):
                for ci in range(len(g[0])):
                    if g[ri][ci] == 1:
                        return ri, ci

        sri, sci = findStartPoint(grid)
        for (rowDiff, colDiff) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nextRow = sri + rowDiff
            nextCol = sci + colDiff
            if nextRow >= 0 and nextRow < rowCount and nextCol >= 0 and nextCol < colCount:
                # is a valid point
                if grid[nextRow][nextCol] == 0:
                    # is a valid path
                    newGrid = []
                    for ri in range(rowCount):
                        newGrid.append(grid[ri][:])
                    newGrid[sri][sci] = -1
                    newGrid[nextRow][nextCol] = 1
                    ans += self.uniquePathsIII(newGrid)
                elif grid[nextRow][nextCol] == 2:
                    shouldBreak = False
                    for ri in range(rowCount):
                        if shouldBreak:
                            break
                        for ci in range(colCount):
                            if shouldBreak:
                                break
                            if grid[ri][ci] == 0:
                                shouldBreak = True
                    if not shouldBreak:
                        ans += 1
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.uniquePathsIII(
            [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]), 2)
        self.assertEqual(solution.uniquePathsIII(
            [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]), 4)
        self.assertEqual(solution.uniquePathsIII([[0, 1], [2, 0]]), 0)


if __name__ == '__main__':
    unittest.main()
