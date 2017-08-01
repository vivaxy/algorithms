"""
https://leetcode.com/problems/zigzag-conversion/

https://leetcode.com/submissions/detail/111991386/
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ''
        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                index = i
                while index < len(s):
                    result += s[index]
                    index += 2 * numRows - 2
                continue
            index = i
            nextType = '/'
            while index < len(s):
                result += s[index]
                if nextType == '/':
                    index += 2 * numRows - 2 - 2 * i
                    nextType = '|'
                    continue
                if nextType == '|':
                    index += 2 * i
                    nextType = '/'
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.convert('ABCDE', 4), 'ABCED')
        self.assertEqual(solution.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')


if __name__ == '__main__':
    unittest.main()
