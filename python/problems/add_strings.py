"""
https://leetcode.com/problems/add-strings/

https://leetcode.com/submissions/detail/106766561/
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1 = len(num1)
        length2 = len(num2)
        length = max(length1, length2)
        result = ''
        remaining = 0
        for i in range(length):
            digital1 = int(num1[length1 - 1 - i]) if length1 > i else 0
            digital2 = int(num2[length2 - 1 - i]) if length2 > i else 0
            sum = digital1 + digital2 + remaining
            remaining = 1 if sum > 9 else 0
            result = str(sum - 10 if sum > 9 else sum) + result
        if remaining != 0:
            result = str(remaining) + result
        return result

import unittest
class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.addStrings('1', '2'), '3')
        self.assertEqual(solution.addStrings('100', '100'), '200')
        self.assertEqual(solution.addStrings('9333852702227987', '85731737104263'), '9419584439332250')
        self.assertEqual(solution.addStrings('1', '9'), '10')

if __name__ == '__main__':
    unittest.main()