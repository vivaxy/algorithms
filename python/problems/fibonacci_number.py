"""
https://leetcode.com/problems/fibonacci-number/


"""


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        ans = 1
        p1 = 0
        p2 = 1
        for i in range(2, N + 1):
            ans = p1 + p2
            p1 = p2
            p2 = ans
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.fib(2), 1)
        self.assertEqual(solution.fib(3), 2)
        self.assertEqual(solution.fib(4), 3)


if __name__ == '__main__':
    unittest.main()
