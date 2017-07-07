"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

https://leetcode.com/submissions/detail/108647269/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for prev, next in zip(prices, prices[1:]):
            p = next - prev
            if p > 0:
                profit += p
        return profit


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([]), 0)
        self.assertEqual(solution.maxProfit([1, 2]), 1)


if __name__ == '__main__':
    unittest.main()
