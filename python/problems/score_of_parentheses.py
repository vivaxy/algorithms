"""
https://leetcode.com/problems/score-of-parentheses/

https://leetcode.com/submissions/detail/187744280/
https://leetcode.com/submissions/detail/187746203/
"""


class Solution1:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        depth = 0
        for i in range(len(S)):
            char = S[i]
            if char == '(':
                depth += 1
                continue
            if char == ')':
                depth -= 1
                if depth == 0:
                    if i == 1:
                        return 1 + self.scoreOfParentheses(S[i+1:])
                    return self.scoreOfParentheses(S[1:i]) * 2 + self.scoreOfParentheses(S[i+1:])
        return 0


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        power = 0
        ans = 0
        opened = False

        for char in S:
            if char == '(':
                power += 1
                opened = True
                continue
            if char == ')':
                power -= 1
                if opened:
                    ans += 2 ** power
                    opened = False
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfParentheses('()'), 1)
        self.assertEqual(solution.scoreOfParentheses('(())'), 2)
        self.assertEqual(solution.scoreOfParentheses('()()'), 2)
        self.assertEqual(solution.scoreOfParentheses('(()(()))'), 6)


if __name__ == '__main__':
    unittest.main()
