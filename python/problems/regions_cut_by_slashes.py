"""
https://leetcode.com/problems/regions-cut-by-slashes/

https://leetcode.com/submissions/detail/217603381/
"""

from typing import List


#  ___
# |\0/|
# |1|2|
# |/3\|
#  ---
class DSU:
    def __init__(self, N: int):
        self.p = list(range(N))

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr # set xr relation to yr


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r + 1 < N:
                    dsu.union(root + 3, (root + 4 * N) + 0)
                if r - 1 >= 0:
                    dsu.union(root + 0, (root - 4 * N) + 3)
                # east/west
                if c + 1 < N:
                    dsu.union(root + 2, (root + 4) + 1)
                if c - 1 >= 0:
                    dsu.union(root + 1, (root - 4) + 2)

        return sum(dsu.find(x) == x for x in range(4 * N * N))


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.regionsBySlashes([
            " /",
            "/ "
        ]), 2)
        self.assertEqual(solution.regionsBySlashes([
            " /",
            "  "
        ]), 1)
        self.assertEqual(solution.regionsBySlashes([
            "\\/",
            "/\\"
        ]), 4)
        self.assertEqual(solution.regionsBySlashes([
            "/\\",
            "\\/"
        ]), 5)
        self.assertEqual(solution.regionsBySlashes([
            "//",
            "/ "
        ]), 3)


if __name__ == '__main__':
    unittest.main()
