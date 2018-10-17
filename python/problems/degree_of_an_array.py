"""
https://leetcode.com/problems/degree-of-an-array/

https://leetcode.com/submissions/detail/130966108/
"""


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for index, num in enumerate(nums):
            if num in d:
                d[num]['end'] = index
                d[num]['count'] += 1
            else:
                d[num] = {
                    'count': 1,
                    'start': index,
                    'end': index,
                }
        maxCount = 0
        minLenght = len(nums)
        for value in d:
            count = d[value]['count']
            if count > maxCount:
                maxCount = count
                minLenght = d[value]['end'] - d[value]['start'] + 1
            elif count == maxCount:
                currentLength = d[value]['end'] - d[value]['start'] + 1
                if minLenght > currentLength:
                    minLenght = currentLength
        return minLenght


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findShortestSubArray([1, 2, 2, 3, 1]), 2)
        self.assertEqual(solution.findShortestSubArray(
            [1, 2, 2, 3, 1, 4, 2]), 6)


if __name__ == '__main__':
    unittest.main()
