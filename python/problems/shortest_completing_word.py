"""
https://leetcode.com/problems/shortest-completing-word/description/


"""


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """



import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.shortestCompletingWord('', []), '')


if __name__ == '__main__':
    unittest.main()
