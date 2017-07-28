"""
https://leetcode.com/problems/spiral-matrix/

https://leetcode.com/submissions/detail/111507683/
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return list(map(lambda li: li[0], matrix))
        x, y, minX, minY, maxX, maxY = 0, 0, 0, 0, len(
            matrix[0]) - 1, len(matrix) - 1
        rList = []
        xDirection = 1
        yDirection = 0
        while minX <= maxX and minY <= maxY:
            rList.append(matrix[y][x])
            x += xDirection
            y += yDirection
            if xDirection == 1 and yDirection == 0 and x >= maxX:
                xDirection = 0
                yDirection = 1
                minY += 1
            if yDirection == 1 and xDirection == 0 and y >= maxY:
                xDirection = -1
                yDirection = 0
                maxX -= 1
            if xDirection == -1 and yDirection == 0 and x <= minX:
                xDirection = 0
                yDirection = -1
                maxY -= 1
            if xDirection == 0 and yDirection == -1 and y <= minY:
                xDirection = 1
                yDirection = 0
                minX += 1
        rList.append(matrix[y][x])
        return rList


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.spiralOrder(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(solution.spiralOrder([[1]]), [1])
        self.assertEqual(solution.spiralOrder([[3], [2]]), [3, 2])


if __name__ == '__main__':
    unittest.main()
