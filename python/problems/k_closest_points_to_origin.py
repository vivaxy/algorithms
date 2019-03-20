"""
https://leetcode.com/problems/k-closest-points-to-origin/

https://leetcode.com/submissions/detail/216118156/
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.kClosest(
            [[1, 3], [-2, 2]], 1),
            [[-2, 2]])
        self.assertEqual(solution.kClosest(
            [[3, 3], [5, -1], [-2, 4]], 2),
            [[3, 3], [-2, 4]])  # or [[-2,4],[3,3]]


if __name__ == '__main__':
    unittest.main()
