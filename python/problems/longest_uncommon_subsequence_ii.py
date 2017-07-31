"""
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

"""


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findLUSlength(''), 0)


if __name__ == '__main__':
    unittest.main()
