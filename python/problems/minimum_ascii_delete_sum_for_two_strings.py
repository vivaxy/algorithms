"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/


"""


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minimumDeleteSum('sea', 'eat'), 231)


if __name__ == '__main__':
    unittest.main()
