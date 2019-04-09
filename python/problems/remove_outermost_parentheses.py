import unittest
"""
https://leetcode.com/problems/remove-outermost-parentheses/

https://leetcode.com/submissions/detail/221110733/
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ''
        depth = 0
        for s in S:
            if s == '(':
                depth += 1
            if depth > 1:
                ans += s
            if s == ')':
                depth -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.removeOuterParentheses(
            '(()())(())'), '()()()')
        self.assertEqual(solution.removeOuterParentheses(
            '(()())(())(()(()))'), '()()()()(())')
        self.assertEqual(solution.removeOuterParentheses('()()'), '')


if __name__ == '__main__':
    unittest.main()
