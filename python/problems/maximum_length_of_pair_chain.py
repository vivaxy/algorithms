"""
https://leetcode.com/problems/maximum-length-of-pair-chain/solution/

https://leetcode.com/submissions/detail/146198048/
"""


class Solution1:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sortedPairs = sorted(pairs)
        pairsLen = len(sortedPairs)
        ans = [1] * pairsLen
        for i in range(pairsLen):
            for j in range(i):
                if sortedPairs[j][1] < sortedPairs[i][0]:
                    ans[i] = max(ans[i], ans[j] + 1)
        return ans[pairsLen - 1]


import operator
import sys

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sortedPairs = sorted(pairs, key=operator.itemgetter(1))
        ans = 0
        cur = -sys.maxsize - 1
        for x, y in sortedPairs:
            if cur < x:
                cur = y
                ans += 1
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findLongestChain(
            [[1, 2], [2, 3], [3, 4]]), 2)


if __name__ == '__main__':
    unittest.main()
