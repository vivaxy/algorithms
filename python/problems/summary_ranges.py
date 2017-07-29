"""
https://leetcode.com/problems/summary-ranges/

https://leetcode.com/submissions/detail/111581979/
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        answer = []
        if len(nums) == 0:
            return answer
        string = ''
        for i in range(0, len(nums) - 1):
            if string == '':
                string = str(nums[i])
            if nums[i] + 1 == nums[i + 1]:
                continue
            if string != str(nums[i]):
                 string += '->' + str(nums[i])
            answer.append(string)
            string = ''
        if string == '':
            answer.append(str(nums[len(nums) - 1]))
        else:
            string += '->' + str(nums[len(nums) - 1])
            answer.append(string)
        return answer


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.summaryRanges(
            [0, 1, 2, 4, 5, 7]), ["0->2", "4->5", "7"])
        self.assertEqual(solution.summaryRanges([]), [])
        self.assertEqual(solution.summaryRanges([1, 3]), ["1", "3"])


if __name__ == '__main__':
    unittest.main()
