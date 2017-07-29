"""
https://leetcode.com/problems/minimum-time-difference/

https://leetcode.com/submissions/detail/111619897/
"""

import sys


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePointsInNumber = []
        for timePoint in timePoints:
            strings = timePoint.split(':')
            timePointsInNumber.append(int(strings[0]) * 60 + int(strings[1]))
        sortedTimePointsInNumber = sorted(timePointsInNumber)
        minDiff = sys.maxsize
        for i in range(0, len(timePoints) - 1):
            diff = sortedTimePointsInNumber[i + 1] - sortedTimePointsInNumber[i]
            if diff < minDiff:
                minDiff = diff
        diff = sortedTimePointsInNumber[0] + (24 * 60) - sortedTimePointsInNumber[len(timePoints) - 1]
        if diff < minDiff:
            minDiff = diff
        return minDiff


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findMinDifference(["23:59", "00:00"]), 1)


if __name__ == '__main__':
    unittest.main()
