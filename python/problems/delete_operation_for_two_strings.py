"""
https://leetcode.com/problems/delete-operation-for-two-strings/


"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """




import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minDistance('sea', 'eat'), 2)


if __name__ == '__main__':
    unittest.main()
