import unittest
"""
https://leetcode.com/problems/minimum-cost-for-tickets/

https://leetcode.com/submissions/detail/227086131/
"""

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.memo = dict()
        # dp(i) = min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp[i + 30] + costs[2])

        def dp(day: int) -> int:
            if day in self.memo:
                return self.memo[day]
            if day > 365:
                return 0
            if day in days:
                ans = min(
                    dp(day + 1) + costs[0], dp(day + 7) + costs[1], dp(day + 30) + costs[2])
                self.memo[day] = ans
                return ans
            ans = dp(day + 1)
            self.memo[day] = ans
            return ans
        return dp(1)


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.mincostTickets(
            [1, 4, 6, 7, 8, 20], [2, 7, 15]), 11)
        self.assertEqual(solution.mincostTickets(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]), 17)


if __name__ == '__main__':
    unittest.main()
