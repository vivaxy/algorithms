"""
https://leetcode.com/problems/smallest-good-base/description/


"""

import math


class Solution:
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        s = int(n)
        for m in range(int(math.log(s, 2)), 1, -1):
            k = int(s ** m ** -1)
            if (k ** (m + 1) - 1) // (k - 1) == s:
                return str(k)
        return str(s - 1)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.smallestGoodBase("6321"), "79")
        self.assertEqual(solution.smallestGoodBase("131407"), "362")
        self.assertEqual(solution.smallestGoodBase('13'), '3')


if __name__ == '__main__':
    unittest.main()
