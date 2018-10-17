"""
https://leetcode.com/problems/number-of-lines-to-write-string/

https://leetcode.com/submissions/detail/147297163/
"""


class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 0
        currentLineWidthLeft = 100
        for char in S:
            charLen = widths[ord(char) - 97]
            if currentLineWidthLeft >= charLen:
                currentLineWidthLeft -= charLen
            else:
                # new line
                lines += 1
                currentLineWidthLeft = 100 - charLen
        # last line
        return [lines + 1, 100 - currentLineWidthLeft]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        # self.assertEqual(solution.numberOfLines([
        #     10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        #     10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
        # ], 'abcdefghijklmnopqrstuvwxyz'), [3, 60])
        self.assertEqual(solution.numberOfLines([
            4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
        ], 'bbbcccdddaaa'), [2, 4])


if __name__ == '__main__':
    unittest.main()
