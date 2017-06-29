"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

https://leetcode.com/submissions/detail/107710289/
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        while index1 < len(numbers):
            value = numbers[index1]
            index2 = index1 + 1
            while index2 < len(numbers):
                if value + numbers[index2] > target:
                    break
                if value + numbers[index2] == target:
                    return [index1 + 1, index2 + 1]
                index2 += 1
            index2 = index1 + 1
            while numbers[index1] == numbers[index2] and index2 < len(numbers):
                index1 += 1
                index2 += 1
            index1 += 1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(solution.twoSum([0, 0, 3, 4], 0), [1, 2])
        self.assertEqual(solution.twoSum([5, 25, 75], 100), [2, 3])

if __name__ == '__main__':
    unittest.main()
