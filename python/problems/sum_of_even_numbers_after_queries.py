"""
https://leetcode.com/problems/sum-of-even-numbers-after-queries/

https://leetcode.com/submissions/detail/215582833/
"""

from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ANS = []
        ans = 0
        for a in A:
            if a % 2 == 0:
                ans += a
        for query in queries:
            [val, index] = query
            A[index] += val
            if A[index] % 2 == 0 and val % 2 == 1:
                ans += A[index]
            elif A[index] % 2 == 0 and val % 2 == 0:
                ans += val
            elif A[index] % 2 == 1 and val % 2 == 1:
                ans -= A[index] - val
            ANS.append(ans)
        return ANS


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.sumEvenAfterQueries(
            [1, 2, 3, 4],
            [[1, 0], [-3, 1], [-4, 0], [2, 3]]),
            [8, 6, 2, 4]
        )


if __name__ == '__main__':
    unittest.main()
