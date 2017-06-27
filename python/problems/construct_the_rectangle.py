"""
https://leetcode.com/problems/construct-the-rectangle/

https://leetcode.com/submissions/detail/107452214/
"""

import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(math.sqrt(area))
        while area % W != 0:
            W -= 1
        return [int(area / W), W]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.constructRectangle(4), [2, 2])


if __name__ == '__main__':
    unittest.main()
