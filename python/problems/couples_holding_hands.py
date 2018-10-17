"""
https://leetcode.com/problems/couples-holding-hands/

https://leetcode.com/submissions/detail/143499206/
"""

import math


class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        def getPartnerValue(value):
            if value % 2 == 0:
                return value + 1
            return value - 1
        fromValueToIndex = {}
        for index in range(len(row)):
            fromValueToIndex[row[index]] = index
        def swap(mapOrArray, fromIndex, toIndex):
            mapOrArray[fromIndex], mapOrArray[toIndex] = mapOrArray[toIndex], mapOrArray[fromIndex]
        for index in range(len(row)):
            swapIndex = getPartnerValue(fromValueToIndex[getPartnerValue(row[index])])
            while swapIndex != index:
                swap(row, index, swapIndex)
                swap(fromValueToIndex, row[index], row[swapIndex])
                ans += 1
                swapIndex = getPartnerValue(fromValueToIndex[getPartnerValue(row[index])])
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minSwapsCouples([0, 2, 4, 6, 7, 1, 3, 5]), 3)
        self.assertEqual(solution.minSwapsCouples([0, 2, 1, 3]), 1)
        self.assertEqual(solution.minSwapsCouples([3, 2, 0, 1]), 0)


if __name__ == '__main__':
    unittest.main()
