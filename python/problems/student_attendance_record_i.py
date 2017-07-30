"""
https://leetcode.com/problems/student-attendance-record-i/

https://leetcode.com/submissions/detail/111728919/
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aCount = 0
        maxCoutinousCCount = 0
        index = 0
        while index < len(s):
            if s[index] == 'A':
                aCount += 1
                index += 1
                continue
            if s[index] == 'L':
                cCount = 1
                index += 1
                while index < len(s) and s[index] == 'L':
                    cCount += 1
                    index += 1
                maxCoutinousCCount = max(maxCoutinousCCount, cCount)
                continue
            index += 1
        if aCount > 1:
            return False
        if maxCoutinousCCount > 2:
            return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.checkRecord('ALLAPPL'), False)
        self.assertEqual(solution.checkRecord('PPALLP'), True)
        self.assertEqual(solution.checkRecord('PPALLL'), False)


if __name__ == '__main__':
    unittest.main()
