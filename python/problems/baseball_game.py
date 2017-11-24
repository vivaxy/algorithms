"""
https://leetcode.com/problems/baseball-game/description/

https://leetcode.com/submissions/detail/129471355/
"""

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for op in ops:
            if op == '+':
                scores.append(scores[-2] + scores[-1])
            elif op == 'D':
                scoresLen = len(scores)
                scores.append(scores[-1] * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)



import unittest

class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.calPoints(['5', '2', 'C', 'D', '+']), 30)

if __name__ == '__main__':
    unittest.main()
