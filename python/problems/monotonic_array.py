"""
https://leetcode.com/problems/monotonic-array/

https://leetcode.com/submissions/detail/186908631/
"""


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direction = 0
        for a, b in zip(A, A[1:]):
            if direction == 0:
                if a == b:
                    continue
                if a < b:
                    direction = 1
                    continue
                if a > b:
                    direction = -1
                    continue
            if direction == -1 and a < b:
                return False
            if direction == 1 and a > b:
                return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.isMonotonic([1, 2, 2, 3]), True)
        self.assertEqual(solution.isMonotonic([6, 5, 4, 4]), True)
        self.assertEqual(solution.isMonotonic([1, 3, 2]), False)
        self.assertEqual(solution.isMonotonic([1, 2, 4, 5]), True)
        self.assertEqual(solution.isMonotonic([1, 1, 1]), True)


if __name__ == '__main__':
    unittest.main()
