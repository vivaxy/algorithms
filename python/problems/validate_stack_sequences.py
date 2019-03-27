"""
https://leetcode.com/problems/validate-stack-sequences/

https://leetcode.com/submissions/detail/218117451/
"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed == popped:
            return True
        a = []
        while len(pushed):
            if len(a) == 0:
                a.append(pushed.pop(0))
            if popped[0] != a[-1]:
                a.append(pushed.pop(0))
            else:
                popped.pop(0)
                a.pop()
        if len(a) != len(popped):
            return False
        while len(a):
            if a.pop() != popped.pop(0):
                return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.validateStackSequences(
            [1, 2, 3, 4, 5],
            [4, 5, 3, 2, 1]), True)
        self.assertEqual(solution.validateStackSequences(
            [1, 2, 3, 4, 5],
            [4, 3, 5, 1, 2]), False)
        self.assertEqual(solution.validateStackSequences(
            [],
            []), True)
        self.assertEqual(solution.validateStackSequences(
            [1, 0],
            [1, 0]), True)
        self.assertEqual(solution.validateStackSequences(
            [0, 2, 1],
            [0, 1, 2]), True)


if __name__ == '__main__':
    unittest.main()
