"""
https://leetcode.com/problems/binary-gap/description/

https://leetcode.com/submissions/detail/182434177/
https://leetcode.com/submissions/detail/182434882/
"""


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        distance = 0
        cur = N
        while cur & 1 == 0:
            cur = cur >> 1
        while cur > 0:
            cur = cur >> 1
            distance += 1
            if cur & 1 == 1:
                ans = max(distance, ans)
                distance = 0
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        # self.assertEqual(solution.binaryGap(22), 2)
        # self.assertEqual(solution.binaryGap(5), 2)
        # self.assertEqual(solution.binaryGap(6), 1)
        self.assertEqual(solution.binaryGap(8), 0)


if __name__ == '__main__':
    unittest.main()
