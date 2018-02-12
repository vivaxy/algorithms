"""
https://leetcode.com/problems/valid-triangle-number/

https://leetcode.com/submissions/detail/140519456/
"""


class Solution1(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(start, l, count):
            if len(l) == 3:
                if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
                    return 1
                return 0
            localCount = 0
            for i in range(start, len(nums)):
                localCount += dfs(i + 1, l + [nums[i]], count)
            return localCount
        return dfs(0, [], 0)


class Solution2(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)

        def binarySearch(aIndex, bIndex, fromIndex, toIndex):
            if sortedNums[aIndex] + sortedNums[bIndex] <= sortedNums[fromIndex]:
                return fromIndex
            if sortedNums[aIndex] + sortedNums[bIndex] > sortedNums[toIndex]:
                return toIndex + 1
            if fromIndex >= toIndex:
                return fromIndex
            if fromIndex == toIndex - 1:
                if sortedNums[aIndex] + sortedNums[bIndex] > sortedNums[toIndex]:
                    return toIndex + 1
                return toIndex
            middleIndex = int((fromIndex + toIndex) / 2)
            if sortedNums[aIndex] + sortedNums[bIndex] > sortedNums[middleIndex]:
                return binarySearch(aIndex, bIndex, middleIndex + 1, toIndex)
            return binarySearch(aIndex, bIndex, fromIndex, middleIndex - 1)
        ans = 0
        for aIndex in range(len(sortedNums) - 2):
            for bIndex in range(aIndex + 1, len(sortedNums) - 1):
                maxCIndex = binarySearch(
                    aIndex, bIndex, bIndex + 1, len(sortedNums) - 1)
                ans += maxCIndex - bIndex - 1
        return ans


class Solution3(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)

        def binarySearch(aIndex, bIndex, _fromIndex, _toIndex):
            fromIndex = _fromIndex
            toIndex = _toIndex
            # why add =? 如果 toIndex 满足条件，那么找到就不是最终的结果了
            while fromIndex <= toIndex:
                middleIndex = int((fromIndex + toIndex) / 2)
                if sortedNums[aIndex] + sortedNums[bIndex] > sortedNums[middleIndex]:
                    fromIndex = middleIndex + 1
                else:
                    toIndex = middleIndex - 1
            return fromIndex
        ans = 0
        for aIndex in range(len(sortedNums) - 2):
            for bIndex in range(aIndex + 1, len(sortedNums) - 1):
                maxCIndex = binarySearch(
                    aIndex, bIndex, bIndex + 1, len(sortedNums) - 1)
                ans += maxCIndex - bIndex - 1
        return ans


class Solution4(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)

        def binarySearch(aIndex, bIndex, _fromIndex, _toIndex):
            fromIndex = _fromIndex
            toIndex = _toIndex
            while fromIndex <= toIndex:
                middleIndex = int((fromIndex + toIndex) / 2)
                if sortedNums[aIndex] + sortedNums[bIndex] > sortedNums[middleIndex]:
                    fromIndex = middleIndex + 1
                else:
                    toIndex = middleIndex - 1
            return fromIndex
        ans = 0
        for aIndex in range(len(sortedNums) - 2):
            if sortedNums[aIndex] <= 0:
                continue
            fromIndex = aIndex + 2
            for bIndex in range(aIndex + 1, len(sortedNums) - 1):
                maxCIndex = binarySearch(
                    aIndex, bIndex, fromIndex, len(sortedNums) - 1)
                # 优化 fromIndex 为上一次的结果
                fromIndex = maxCIndex
                ans += maxCIndex - bIndex - 1
        return ans


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)
        ans = 0
        for aIndex in range(len(sortedNums) - 2):
            if sortedNums[aIndex] <= 0:
                continue
            cIndex = aIndex + 2
            for bIndex in range(aIndex + 1, len(sortedNums) - 1):
                while cIndex < len(sortedNums) and sortedNums[aIndex] + sortedNums[bIndex] > sortedNums[cIndex]:
                    cIndex += 1
                ans += cIndex - bIndex - 1
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.triangleNumber([0, 1, 0, 1]), 0)
        self.assertEqual(solution.triangleNumber([48, 66, 61, 46, 94, 75]), 19)
        self.assertEqual(solution.triangleNumber([1, 1, 3, 4]), 0)
        self.assertEqual(solution.triangleNumber([2, 2, 3, 4]), 3)


if __name__ == '__main__':
    unittest.main()
