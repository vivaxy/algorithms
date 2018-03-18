"""
https://leetcode.com/problems/generate-parentheses/description/

https://leetcode.com/submissions/detail/145650277/
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def recurse(curStr, lefts, rights, limit):
            if lefts == limit and rights == limit:
                return ans.append(curStr)
            if lefts == limit:
                return recurse(curStr + ')', lefts, rights + 1, limit)
            recurse(curStr + '(', lefts + 1, rights, limit)
            if rights < lefts:
                recurse(curStr + ')', lefts, rights + 1, limit)
        recurse('', 0, 0, n)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.generateParenthesis(3), [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ])


if __name__ == '__main__':
    unittest.main()
