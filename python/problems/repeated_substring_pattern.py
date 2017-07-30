"""
https://leetcode.com/problems/repeated-substring-pattern/

https://leetcode.com/submissions/detail/111731778/
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        factors = []
        option = 1
        while option <= int(len(s) / 2):
            if len(s) % option == 0:
                factors.append(option)
            option += 1
        for patternLen in factors:
            # each patter len, 2 or 5
            # if a ptetternLen passed return True
            passed = True
            for i in range(0, patternLen):
                # each pattern char
                # if all pattern char same, pass
                char = ''
                thisCharSame = True
                for strIndex in range(0, int(len(s) / patternLen)):
                    if char == '':
                        char = s[patternLen * strIndex + i]
                        continue
                    if char != s[patternLen * strIndex + i]:
                        thisCharSame = False
                        break
                if not thisCharSame:
                    passed = False
                    break
            if passed:
                return True
        return False


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.repeatedSubstringPattern('abcabc'), True)
        self.assertEqual(solution.repeatedSubstringPattern('a'), False)
        self.assertEqual(solution.repeatedSubstringPattern('abab'), True)
        self.assertEqual(solution.repeatedSubstringPattern('abac'), False)
        self.assertEqual(solution.repeatedSubstringPattern('aba'), False)


if __name__ == '__main__':
    unittest.main()
