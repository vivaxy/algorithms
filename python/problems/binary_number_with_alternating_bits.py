"""
https://leetcode.com/problems/binary-number-with-alternating-bits/description/

https://leetcode.com/submissions/detail/129676755/
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isAlternating = True
        prevDigital = n % 2
        nextN = int(n / 2)
        while nextN > 0:
            remaining = nextN % 2
            nextN = int(nextN / 2)
            if remaining == prevDigital:
                return False
            prevDigital = remaining
        return isAlternating


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.hasAlternatingBits(5), True)
        self.assertEqual(solution.hasAlternatingBits(10), True)
        self.assertEqual(solution.hasAlternatingBits(7), False)
        self.assertEqual(solution.hasAlternatingBits(11), False)


if __name__ == '__main__':
    unittest.main()
