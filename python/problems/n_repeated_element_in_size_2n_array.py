"""
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

https://leetcode.com/submissions/detail/213153690/
"""

from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)):
            for j in range(i):
                if A[i] == A[j]:
                    return A[i]
        return None


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.repeatedNTimes([1, 2, 3, 3]), 3)
        self.assertEqual(solution.repeatedNTimes([2, 1, 2, 5, 3, 2]), 2)
        self.assertEqual(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]), 5)


if __name__ == '__main__':
    unittest.main()
