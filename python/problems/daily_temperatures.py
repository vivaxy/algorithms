"""
https://leetcode.com/problems/daily-temperatures/description/

https://leetcode.com/submissions/detail/137437366/
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temperaturesLength = len(temperatures)
        result = [0] * temperaturesLength
        stack = [] # 从大到小
        for index in range(temperaturesLength - 1, -1, -1):
            while len(stack) and temperatures[stack[-1]] <= temperatures[index]:
                stack.pop()
            if len(stack):
                result[index] = stack[-1] - index
            stack.append(index)
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0]
        )


if __name__ == '__main__':
    unittest.main()
