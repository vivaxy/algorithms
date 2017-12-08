"""
https://leetcode.com/problems/palindromic-substrings/description/

https://leetcode.com/submissions/detail/131208078/
"""


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        resultCount = 0
        for index in range(len(s) * 2 - 1):
            if index % 2 == 0:
                offset = 0
                sIndex = int(index / 2)
                while sIndex - offset >= 0 and sIndex + offset < len(s) and s[sIndex - offset] == s[sIndex + offset]:
                    resultCount += 1
                    offset += 1
            else:
                offset = 0
                sIndexLeft = int((index - 1) / 2)
                sIndexRight = int((index + 1) / 2)
                while sIndexLeft - offset >= 0 and sIndexRight + offset < len(s) and s[sIndexLeft - offset] == s[sIndexRight + offset]:
                    resultCount += 1
                    offset += 1
        return resultCount


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.countSubstrings('abc'), 3)
        self.assertEqual(solution.countSubstrings('aaa'), 6)


if __name__ == '__main__':
    unittest.main()
