"""
https://leetcode.com/problems/matrix-cells-in-distance-order/

https://leetcode.com/submissions/detail/224443995/
"""

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[r0, c0]]
        distance = 0
        while len(ans) < R * C:
            distance += 1
            for dr in range(-distance, distance + 1):
                if r0 + dr < 0 or r0 + dr >= R:
                    continue
                dc = distance - abs(dr)
                if c0 + dc >= 0 and c0 + dc < C:
                    ans.append([r0 + dr, c0 + dc])
                if dc == 0:
                    continue
                if c0 - dc >= 0 and c0 - dc < C:
                    ans.append([r0 + dr, c0 - dc])
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.allCellsDistOrder(
            1, 2, 0, 0), [[0, 0], [0, 1]])
        self.assertEqual(solution.allCellsDistOrder(
            2, 2, 0, 1), [[0, 1], [0, 0], [1, 1], [1, 0]])
        self.assertEqual(solution.allCellsDistOrder(2, 3, 1, 2), [
                         [1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]])


if __name__ == '__main__':
    unittest.main()
