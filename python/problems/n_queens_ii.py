"""
https://leetcode.com/problems/n-queens-ii/description/

https://leetcode.com/submissions/detail/149697453/
"""


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        self.dfs([-1] * n, 0)
        return self.ans

    def dfs(self, nums, index):
        if index == len(nums):
            self.ans += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index + 1)

    def valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[n] - nums[i]) == n - i:
                return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.totalNQueens(8), 92)
        self.assertEqual(solution.totalNQueens(4), 2)


if __name__ == '__main__':
    unittest.main()
