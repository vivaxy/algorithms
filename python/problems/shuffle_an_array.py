"""
https://leetcode.com/problems/shuffle-an-array/

https://leetcode.com/submissions/detail/109797134/
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.resetShuffle()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def resetShuffle(self):
        self.indexes = [i for i, num in enumerate(self.nums)]

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if len(self.nums) < 2:
            return self.nums
        def getNextStep(indexes):
            if len(indexes) < 2:
                return None
            prev = indexes[0]
            nextStep = getNextStep(indexes[1:])
            if nextStep:
                return [prev] + nextStep
            current = indexes[1]
            if prev < current:
                nextIndexes = sorted(indexes)
                nextIndex = nextIndexes[nextIndexes.index(prev) + 1]
                nextIndexes.remove(nextIndex)
                return [nextIndex] + nextIndexes
            return None
        self.indexes = getNextStep(self.indexes)
        if not self.indexes:
            self.resetShuffle()
        nums = []
        for i in self.indexes:
            nums.append(self.nums[i])
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


import unittest


class Test(unittest.TestCase):
    def test(self):
        nums1 = [1, 2, 3]
        obj1 = Solution(nums1)
        param_11 = obj1.reset()
        param_21 = obj1.shuffle()
        self.assertEqual(param_11, nums1)
        self.assertNotEqual(param_21, nums1)


if __name__ == '__main__':
    unittest.main()
