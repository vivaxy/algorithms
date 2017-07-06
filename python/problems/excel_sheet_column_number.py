"""
https://leetcode.com/problems/excel-sheet-column-number/

https://leetcode.com/submissions/detail/108517524/
"""

import functools


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return functools.reduce(lambda acc, cur: acc * 26 + cur, map(lambda char: ord(char) - 64, list(s)), 0)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.titleToNumber('A'), 1)
        self.assertEqual(solution.titleToNumber('AA'), 27)


if __name__ == '__main__':
    unittest.main()
