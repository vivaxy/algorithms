"""
https://leetcode.com/problems/stone-game/

https://leetcode.com/submissions/detail/183361768/
"""


class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.stoneGame([5, 3, 4, 5]), True)


if __name__ == '__main__':
    unittest.main()
