"""
https://leetcode.com/problems/interval-list-intersections/

https://leetcode.com/submissions/detail/216951737/
"""

from typing import List

# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        if not len(A) or not len(B):
            return []
        if A[0].end < B[0].start:
            # A: |__|
            # B:      |__|
            return self.intervalIntersection(A[1:], B)
        if A[0].start > B[0].end:
            # A:      |__|
            # B: |__|
            return self.intervalIntersection(A, B[1:])
        if A[0].end <= B[0].end and A[0].end >= B[0].start:
            # 1:
            # A:  |_|
            # B: |___|
            # 2:
            # A: |__|
            # B:  |__|
            return [Interval(max(A[0].start, B[0].start), min(A[0].end, B[0].end))] + self.intervalIntersection(A[1:], B)
        if B[0].end <= A[0].end and B[0].end >= A[0].start:
            # 1:
            # A: |___|
            # B:  |_|
            # 2:
            # A:  |__|
            # B: |__|
            return [Interval(max(A[0].start, B[0].start), min(A[0].end, B[0].end))] + self.intervalIntersection(A, B[1:])
        raise Exception('error condition')


import unittest


class Test(unittest.TestCase):
    def listToInterval(self, A: List[List[int]]) -> List[Interval]:
        return list(map(lambda x: Interval(x[0], x[1]), A))

    def intervalsToList(self, intervals: List[Interval]):
        return list(map(lambda x: [x.start, x.end], intervals))

    def test(self):
        solution = Solution()
        self.assertEqual(self.intervalsToList(solution.intervalIntersection(
            self.listToInterval([[0, 2], [5, 10], [13, 23], [24, 25]]),
            self.listToInterval([[1, 5], [8, 12], [15, 24], [25, 26]]))),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])
        self.assertEqual(self.intervalsToList(solution.intervalIntersection(
            self.listToInterval([[3, 5], [9, 20]]),
            self.listToInterval([[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]))),
            [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]])


if __name__ == '__main__':
    unittest.main()
