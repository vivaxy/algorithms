"""
https://leetcode.com/problems/shortest-palindrome/

"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        for i in range(len(s) - 1, -1, -1):
            if i % 2 == 1:
                # within two letters
                palindrome = ''
                prevIndex = int(i / 2)
                diff = 0
                while prevIndex - diff >= 0 and prevIndex + diff + 1 < len(s) and s[prevIndex - diff] == s[prevIndex + diff + 1]:
                    palindrome = s[prevIndex - diff] + palindrome + s[prevIndex + diff + 1]
                    diff += 1
                if prevIndex - diff == -1:
                    # ok
                    remaingString = s[prevIndex + diff + 1:]
                    for string in remaingString:
                        palindrome = string + palindrome + string
                    return palindrome
            else:
                # on letter
                index = int(i / 2)
                palindrome = s[index]
                diff = 1
                while index - diff >= 0 and index + diff < len(s) and s[index - diff] == s[index + diff]:
                    palindrome = s[index - diff] + palindrome + s[index - diff]
                    diff += 1
                if index - diff == -1:
                    # ok
                    remaingString = s[index + diff:]
                    for string in remaingString:
                        palindrome = string + palindrome + string
                    return palindrome


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.shortestPalindrome('abcd'), 'dcbabcd')
        self.assertEqual(solution.shortestPalindrome('aacecaaa'), 'aaacecaaa')


if __name__ == '__main__':
    unittest.main()
