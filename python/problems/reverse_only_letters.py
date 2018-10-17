"""
https://leetcode.com/problems/reverse-only-letters/

https://leetcode.com/submissions/detail/181196020/
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        asciiLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        letters = ''
        for i in range(len(S) - 1, -1, -1):
            char = S[i]
            if char in asciiLetters:
                letters += char
        i = 0
        ans = ''
        for char in S:
            if char in asciiLetters:
                ans += letters[i]
                i += 1
            else:
                ans += char
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.reverseOnlyLetters('ab-cd'), 'dc-ba')
        self.assertEqual(solution.reverseOnlyLetters(
            'a-bC-dEf-ghIj'), 'j-Ih-gfE-dCba')
        self.assertEqual(solution.reverseOnlyLetters(
            'Test1ng-Leet=code-Q!'), 'Qedo1ct-eeLg=ntse-T!')


if __name__ == '__main__':
    unittest.main()
