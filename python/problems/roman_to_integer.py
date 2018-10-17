"""
https://leetcode.com/problems/roman-to-integer/

https://leetcode.com/submissions/detail/130844466/
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        totalValue = 0
        prevValue = 0
        sArray = list(s)
        sArray.reverse()
        for char in sArray:
            value = dic[char]
            if value >= prevValue:
                totalValue += value
            else:
                totalValue -= value
            prevValue = value
        return totalValue


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('I'), 1)
        self.assertEqual(solution.romanToInt('IV'), 4)


if __name__ == '__main__':
    unittest.main()
