"""
https://leetcode.com/problems/to-lower-case/

https://leetcode.com/submissions/detail/175937795/
"""

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


import unittest

class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.toLowerCase('Hello'), 'hello')
        self.assertEqual(solution.toLowerCase('here'), 'here')
        self.assertEqual(solution.toLowerCase('LOVELY'), 'lovely')

if __name__ == '__main__':
    unittest.main()
