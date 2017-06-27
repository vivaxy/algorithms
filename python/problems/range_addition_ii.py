"""
https://leetcode.com/problems/range-addition-ii/

https://leetcode.com/submissions/detail/107448225/
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for op in ops:
            if op[0] < m:
                m = op[0]
            if op[1] < n:
                n = op[1]
        return m * n


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxCount(3, 3, [[2, 2], [3, 3]]), 4)


if __name__ == '__main__':
    unittest.main()
