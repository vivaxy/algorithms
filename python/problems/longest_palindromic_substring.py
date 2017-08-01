"""
https://leetcode.com/problems/longest-palindromic-substring/

https://leetcode.com/submissions/detail/112032180/
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        for i in range(0, len(s) * 2 - 1):
            if i % 2 == 0:
                # on number
                index = int(i / 2)
                string = s[index]
                diff = 1
                while index - diff >= 0 and index + diff < len(s) and s[index - diff] == s[index + diff]:
                    string = s[index - diff] + string + s[index - diff]
                    diff += 1
                if len(string) > len(longest):
                    longest = string
            else:
                leftIndex = int(i / 2)
                rightIndex = leftIndex + 1
                diff = 0
                string = ''
                while leftIndex - diff >= 0 and rightIndex + diff < len(s) and s[leftIndex - diff] == s[rightIndex + diff]:
                    string = s[leftIndex - diff] + string + s[leftIndex - diff]
                    diff += 1
                if len(string) > len(longest):
                    longest = string
        return longest


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome('babad'), 'bab')


if __name__ == '__main__':
    unittest.main()
