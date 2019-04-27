"""
https://leetcode.com/problems/divisor-game/

https://leetcode.com/submissions/detail/225249529/
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.divisorGame(2), True)
        self.assertEqual(solution.divisorGame(3), False)


if __name__ == '__main__':
    unittest.main()
