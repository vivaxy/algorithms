"""
https://leetcode.com/problems/can-place-flowers/

https://leetcode.com/submissions/detail/111576787/
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                if i != 0:
                    # has prev
                    if i < len(flowerbed) - 1:
                        # has next
                        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                            flowerbed[i] = 1
                            count += 1
                    else:
                        # no next
                        if flowerbed[i - 1] == 0:
                            flowerbed[i] = 1
                            count += 1
                else:
                    # no prev
                    if i < len(flowerbed) - 1:
                        # has next
                        if flowerbed[i + 1] == 0:
                            flowerbed[i] = 1
                            count += 1
                    else:
                        # no next
                        flowerbed[i] = 1
                        count += 1
        return count >= n


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1), True)
        self.assertEqual(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2), False)
        self.assertEqual(solution.canPlaceFlowers(
            [1, 0, 0, 0, 0, 1], 2), False)


if __name__ == '__main__':
    unittest.main()
