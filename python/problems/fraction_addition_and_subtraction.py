"""
https://leetcode.com/problems/fraction-addition-and-subtraction/

https://leetcode.com/submissions/detail/108134733/
"""

import math


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        resultNumerator = 0
        resultDenominator = 1
        symbol = 1
        temp = ''
        numerator = 0
        denominator = 1
        for char in expression:
            if char == '-' or char == '+':
                if temp != '':
                    denominator = int(temp)
                    resultNumerator = resultNumerator * denominator + \
                        symbol * numerator * resultDenominator
                    resultDenominator *= denominator
                    numerator = 0
                    denominator = 1
                    temp = ''
                if char == '-':
                    symbol = -1
                else:
                    symbol = 1
            elif char == '/':
                numerator = int(temp)
                temp = ''
            else:
                temp += char
        denominator = int(temp)
        resultNumerator = resultNumerator * denominator + \
            symbol * numerator * resultDenominator
        resultDenominator *= denominator
        g = math.gcd(resultNumerator, resultDenominator)
        resultDenominator //= g
        resultNumerator //= g
        return str(resultNumerator) + '/' + str(resultDenominator)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.fractionAddition('-1/2+1/2'), '0/1')


if __name__ == '__main__':
    unittest.main()
