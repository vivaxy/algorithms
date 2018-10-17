"""
https://leetcode.com/problems/smallest-range-i/

https://leetcode.com/submissions/detail/178282314/
"""


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxA = None
        minA = None
        for a in A:
            if maxA == None or maxA < a:
                maxA = a
            if minA == None or minA > a:
                minA = a
        ans = maxA - minA - K - K
        if ans < 0:
            return 0
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.smallestRangeI([1], 0), 0)
        self.assertEqual(solution.smallestRangeI([0, 10], 2), 6)
        self.assertEqual(solution.smallestRangeI([1, 3, 6], 3), 0)


if __name__ == '__main__':
    unittest.main()
