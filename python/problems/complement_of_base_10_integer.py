"""
https://leetcode.com/problems/complement-of-base-10-integer/

https://leetcode.com/submissions/detail/217860412/
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        def bc(N: int) -> int:
            if N == 0:
                return 0
            remaining = 1 - N % 2
            n = bc(int(N / 2))
            return remaining + 2 * n
        return bc(N)



import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.bitwiseComplement(5), 2)
        self.assertEqual(solution.bitwiseComplement(7), 0)
        self.assertEqual(solution.bitwiseComplement(10), 5)
        self.assertEqual(solution.bitwiseComplement(0), 1)


if __name__ == '__main__':
    unittest.main()
