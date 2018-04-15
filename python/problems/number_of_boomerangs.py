"""
https://leetcode.com/problems/number-of-boomerangs/description/

https://leetcode.com/submissions/detail/150036781/
"""


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(i, j):
            diffX = i[0] - j[0]
            diffY = i[1] - j[1]
            return diffX * diffX + diffY * diffY
        ans = 0
        for p in points:
            distanceDict = {}
            for q in points:
                dis = distance(p, q)
                if dis in distanceDict:
                    distanceDict[dis] += 1
                else:
                    distanceDict[dis] = 1
            for dis in distanceDict:
                count = distanceDict[dis]
                ans += count * (count - 1)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numberOfBoomerangs(
            [[0, 0], [1, 0], [2, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
