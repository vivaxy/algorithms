"""
https://leetcode.com/problems/reverse-words-in-a-string/

https://leetcode.com/submissions/detail/111619288/
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        word = ''
        for i in range(0, len(s)):
            if s[i] == ' ':
                if word != '':
                    if result == '':
                        result = word
                    else:
                        result = word + ' ' + result
                    word = ''
            else:
                word = word + s[i]
        if word != '':
            if result == '':
                result = word
            else:
                result = word + ' ' + result
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.reverseWords(
            'the sky is blue'), 'blue is sky the')
        self.assertEqual(solution.reverseWords('a'), 'a')


if __name__ == '__main__':
    unittest.main()
