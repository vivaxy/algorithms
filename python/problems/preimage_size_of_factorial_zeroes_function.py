"""
https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

https://leetcode.com/submissions/detail/145351406/
"""


class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def nzero(n):
            factor = 5
            count = 0
            while n >= factor:
                count += n // factor
                factor *= 5
            return count
        if K == 0:
            return 5

        min = 1
        max = K * 5
        while min < max:
            mid = (min + max) // 2
            if nzero(mid) < K:
                min = mid + 1
            else:
                max = mid

        if nzero(min) != K:
            return 0
        else:
            return 5


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.preimageSizeFZF(0), 5)
        self.assertEqual(solution.preimageSizeFZF(5), 0)


if __name__ == '__main__':
    unittest.main()
