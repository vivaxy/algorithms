"""
https://leetcode.com/problems/pancake-sorting/

https://leetcode.com/submissions/detail/217123001/
"""

from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if not len(A):
            return []
        mi = 0
        for i in range(len(A)):
            if A[i] >= A[mi]:
                mi = i
        if mi == len(A) - 1:
            return self.pancakeSort(A[:-1])
        if mi == 0:
            return [len(A)] + self.pancakeSort(A[:0:-1])
        return [mi + 1, len(A)] + self.pancakeSort(A[:mi:-1] + A[:mi])


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.pancakeSort([3, 2, 4, 1]), [3, 4, 2, 3, 2])
        self.assertEqual(solution.pancakeSort([1, 2, 3]), [])
        self.assertEqual(solution.pancakeSort([1, 4, 2, 3]), [2, 4, 3])
        self.assertEqual(solution.pancakeSort([3, 1, 2]), [3, 2])


if __name__ == '__main__':
    unittest.main()
