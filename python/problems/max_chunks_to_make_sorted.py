"""
https://leetcode.com/problems/max-chunks-to-make-sorted/description/

https://leetcode.com/submissions/detail/146477240/
"""


class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        currentRangeMaxIndex = 0
        cursor = 0
        while cursor < len(arr):
            num = arr[cursor]
            currentRangeMaxIndex = max(currentRangeMaxIndex, num)
            if cursor == currentRangeMaxIndex:
                ans += 1
            cursor += 1
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxChunksToSorted([4, 3, 2, 1, 0]), 1)
        self.assertEqual(solution.maxChunksToSorted([1, 0, 2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
