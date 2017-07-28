"""
https://leetcode.com/problems/next-permutation/

https://leetcode.com/submissions/detail/111509916/
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                # find the next larger than nums[i] in nums[i + 1:]
                nextLargetIndex = i + 1
                for j in range(i + 1, len(nums)):
                    if nums[nextLargetIndex] > nums[j] and nums[i] < nums[j]:
                        nextLargetIndex = j
                nums[i], nums[nextLargetIndex] = nums[nextLargetIndex], nums[i]

                def quickSort(a, start, end):
                    i = start
                    j = end
                    k = a[i]
                    while i < j:
                        while i < j and k <= a[j]:
                            j -= 1
                        temp = a[j]
                        a[j] = k
                        a[i] = temp
                        while i < j and k >= a[i]:
                            i += 1
                        temp = a[i]
                        a[i] = k
                        a[j] = temp
                    if start < i - 1:
                        quickSort(a, start, i - 1)
                    if end > i + 1:
                        quickSort(a, i + 1, end)

                quickSort(nums, i + 1, len(nums) - 1)

                return
        for i in range(0, int(len(nums) / 2)):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        input1 = [1, 2, 3]
        solution.nextPermutation(input1)
        self.assertEqual(input1, [1, 3, 2])
        input2 = [3, 2, 1]
        solution.nextPermutation(input2)
        self.assertEqual(input2, [1, 2, 3])
        input3 = [1, 1, 5]
        solution.nextPermutation(input3)
        self.assertEqual(input3, [1, 5, 1])
        input4 = [1, 3, 2]
        solution.nextPermutation(input4)
        self.assertEqual(input4, [2, 1, 3])
        input5 = [2, 3, 1]
        solution.nextPermutation(input5)
        self.assertEqual(input5, [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
