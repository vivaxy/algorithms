"""
https://leetcode.com/problems/judge-route-circle/

https://leetcode.com/submissions/detail/129339056/
https://leetcode.com/submissions/detail/129339394/
"""


class Solution1:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        place = [0, 0]
        for move in moves:
            if move == 'U':
                place[0] -= 1
            if move == 'D':
                place[0] += 1
            if move == 'L':
                place[1] -= 1
            if move == 'R':
                place[1] += 1
        if place[0] == 0 and place[1] == 0:
            return True
        return False


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.judgeCircle('UD'), True)
        self.assertEqual(solution.judgeCircle('LL'), False)


if __name__ == '__main__':
    unittest.main()
