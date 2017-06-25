"""
https://leetcode.com/problems/move-zeroes/

https://leetcode.com/submissions/detail/107207358/
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        zeroes = 0
        while index < len(nums):
            if nums[index] == 0:
                zeroes += 1
                nums.pop(index)
            else:
                index += 1
        while zeroes > 0:
            nums.append(0)
            zeroes -= 1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        input1 = [0, 1, 0, 3, 12]
        solution.moveZeroes(input1)
        self.assertEqual(input1, [1, 3, 12, 0, 0])


if __name__ == '__main__':
    unittest.main()
