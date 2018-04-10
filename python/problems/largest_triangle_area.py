"""
https://leetcode.com/problems/largest-triangle-area/description/

https://leetcode.com/submissions/detail/149320592/
"""


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def calc(a, b, c):
            return abs(a[0] * b[1] + a[1] * c[0] + b[0] * c[1] - a[0] * c[1] - a[1] * b[0] - b[1] * c[0]) / 2
        ans = [0]

        def traverse(arr, startingIndex):
            if len(arr) == 3:
                size = calc(arr[0], arr[1], arr[2])
                if size > ans[0]:
                    ans[0] = size
                return
            if startingIndex >= len(points):
                return
            for index in range(startingIndex, len(points)):
                traverse(arr + [points[index]], index)
        traverse([], 0)
        return ans[0]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.largestTriangleArea(
            [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
