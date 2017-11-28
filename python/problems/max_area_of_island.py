"""
https://leetcode.com/problems/max-area-of-island/description/


"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        gridRowCount = len(grid)
        for row in range(gridRowCount):
            gridColCount = len(grid[row])
            for col in range(gridColCount):
                value = grid[row][col]
                if value == 1:
                    currentArea = 0
                    traversed = []
                    candidates = []
                    candidates.append({'row': row, 'col': col})
                    while len(candidates) > 0:
                        curr = candidates.pop(0)
                        if curr in traversed:
                            continue
                        traversed.append(curr)
                        currentArea += 1
                        # up
                        if curr['row'] - 1 >= 0 and grid[curr['row'] - 1][curr['col']] == 1:
                            candidates.append(
                                {'row': curr['row'] - 1, 'col': curr['col']})
                        # down
                        if curr['row'] + 1 < gridRowCount and grid[curr['row'] + 1][curr['col']] == 1:
                            candidates.append(
                                {'row': curr['row'] + 1, 'col': curr['col']})
                        # left
                        if curr['col'] - 1 >= 0 and grid[curr['row']][curr['col'] - 1] == 1:
                            candidates.append(
                                {'row': curr['row'], 'col': curr['col'] - 1})
                        # right
                        if curr['col'] + 1 < gridColCount and grid[curr['row']][curr['col'] + 1] == 1:
                            candidates.append(
                                {'row': curr['row'], 'col': curr['col'] + 1})
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
