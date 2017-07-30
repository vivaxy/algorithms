"""
https://leetcode.com/problems/count-and-say/

https://leetcode.com/submissions/detail/111734018/
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        nextResult = ''
        count = 1
        while count < n:
            count += 1
            i = 0
            while i < len(result):
                char = result[i]
                charCount = 1
                i += 1
                while i < len(result) and char == result[i]:
                    charCount += 1
                    i += 1
                nextResult += str(charCount) + char
            result = nextResult
            nextResult = ''
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(6), '312211')
        self.assertEqual(solution.countAndSay(5), '111221')
        self.assertEqual(solution.countAndSay(4), '1211')
        self.assertEqual(solution.countAndSay(1), '1')


if __name__ == '__main__':
    unittest.main()
