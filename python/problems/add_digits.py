"""
https://leetcode.com/problems/add-digits/

https://leetcode.com/submissions/detail/106673041/
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num - 1) % 9 + 1

import unittest
class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.addDigits(38), 2)
        self.assertEqual(solution.addDigits(9), 9)
        self.assertEqual(solution.addDigits(0), 0)

if __name__ == '__main__':
    unittest.main()
