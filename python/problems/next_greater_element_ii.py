"""
https://leetcode.com/problems/next-greater-element-ii/
这是个数组，最后一个值的后一个值是第一个值
要返回一个数组，这个数组中的值是这个位置的后面第一个比它大的值

O(n) 的复杂度
https://leetcode.com/submissions/detail/107624235/
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st, res = [], [-1] * len(nums)
        for idx, i in enumerate(nums * 2):
            while st and (nums[st[-1]] < i):
                res[st.pop()] = i
            if idx < len(nums):
                st.append(idx)
        return res


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.nextGreaterElements([1, 2, 1]), [2, -1, 2])


if __name__ == '__main__':
    unittest.main()
