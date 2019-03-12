"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/

https://leetcode.com/submissions/detail/214362635/
"""

from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sortedDeck = sorted(deck)
        ans = []
        while len(sortedDeck):
            card = sortedDeck.pop()
            if len(ans):
                ans.insert(0, ans.pop())
            ans.insert(0, card)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.deckRevealedIncreasing(
            [17, 13, 11, 2, 3, 5, 7]), [2, 13, 3, 11, 5, 17, 7])


if __name__ == '__main__':
    unittest.main()
