"""
https://leetcode.com/problems/squares-of-a-sorted-array/

https://leetcode.com/submissions/detail/213851415/
"""

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        while len(A):
            num = A.pop() if abs(A[0]) < abs(A[-1]) else A.pop(0)
            ans.insert(0, num * num)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.sortedSquares(
            [-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(solution.sortedSquares(
            [-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])
        self.assertEqual(solution.sortedSquares([0, 1, 3, 4]), [0, 1, 9, 16])


if __name__ == '__main__':
    unittest.main()
