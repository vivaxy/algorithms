"""
https://www.geeksforgeeks.org/reservoir-sampling/
http://en.wikipedia.org/wiki/Reservoir_sampling
"""

import random


class ReserviorSampling(object):
    def selectKItems(self, stream, n, k):
        """
        :type stream: List[int]
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = []
        for index in range(k):
            ans.append(stream[index])
        for index in range(k, n):
            randomIndex = random.randrange(0, index)
            if randomIndex < k:
                ans[randomIndex] = stream[index]
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        reserviorSampling = ReserviorSampling()
        sample = reserviorSampling.selectKItems(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1)
        self.assertEqual(len(sample), 1)
        sample = reserviorSampling.selectKItems(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 5)
        self.assertEqual(len(sample), 5)
        sample = reserviorSampling.selectKItems(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10)
        self.assertEqual(len(sample), 10)


if __name__ == '__main__':
    unittest.main()
