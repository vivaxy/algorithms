"""
https://leetcode.com/problems/fair-candy-swap/

https://leetcode.com/submissions/detail/186770998/
"""


class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A) - sum(B)) / 2
        setB = set(B)
        for a in A:
            if a - diff in setB:
                return [a, a - diff]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.fairCandySwap([1, 1], [2, 2]), [1, 2])
        self.assertEqual(solution.fairCandySwap([1, 2], [2, 3]), [1, 2])
        self.assertEqual(solution.fairCandySwap([2], [1, 3]), [2, 3])
        self.assertEqual(solution.fairCandySwap([1, 2, 5], [2, 4]), [5, 4])


if __name__ == '__main__':
    unittest.main()
