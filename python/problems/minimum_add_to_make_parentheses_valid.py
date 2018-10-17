"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

https://leetcode.com/submissions/detail/182907873/
"""


class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = 0
        depth = 0
        for char in S:
            if char == '(':
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    depth += 1
                    ans += 1
        return ans + depth


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minAddToMakeValid("())"), 1)
        self.assertEqual(solution.minAddToMakeValid("((("), 3)
        self.assertEqual(solution.minAddToMakeValid("()"), 0)
        self.assertEqual(solution.minAddToMakeValid("()))(("), 4)


if __name__ == '__main__':
    unittest.main()
