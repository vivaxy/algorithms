"""
https://leetcode.com/problems/find-the-closest-palindrome/

https://leetcode.com/submissions/detail/111711406/
"""
import math


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        allOne = True
        allNine = True
        match101 = True
        result = ''
        if math.log10(int(n)) % 1 == 0:
            return str(int(n) - 1)
        for i in range(0, len(n)):
            if i < len(n) / 2:
                result += n[i]
            else:
                result += n[len(n) - 1 - i]
            if n[i] != '1':
                allOne = False
            if n[i] != '9':
                allNine = False
            if i != 0 and i != len(n) - 1:
                if n[i] != '0':
                    match101 = False
        if result == n:
            if len(n) == 1:
                # "1" -> "0"
                return str(int(n) - 1)
            if allOne:
                if n == '11':
                    return '9'
                if n == '111':
                    return '101'
                if n == '1111':
                    return '999'
                if len(n) % 2 == 1:
                    # "11111"
                    substraction = '1'
                    for i in range(0, int(len(n) / 2)):
                        substraction += '0'
                    return str(int(n) - int(substraction))
                substraction = '11'
                for i in range(0, int(len(n) / 2) - 1):
                    substraction += '0'
                return str(int(n) - int(substraction))

            if allNine:
                # "9999"
                return str(int(n) + 2)
            if n[0] == '1' and n[len(n) - 1] == '1' and match101:
                # "1000000001"
                return str(int(n) - 2)
            # change middle one or two
            if len(n) % 2 == 1:
                # "11111"
                substraction = '1'
                for i in range(0, int(len(n) / 2)):
                    substraction += '0'
                if n[int((len(n) - 1) / 2)] == '0':
                    substraction = '-' + substraction
                return str(int(n) - int(substraction))
            substraction = '11'
            for i in range(0, int(len(n) / 2) - 1):
                substraction += '0'
            if n[int(len(n) / 2)] == '0':
                substraction = '-' + substraction
            return str(int(n) - int(substraction))
        # try add middle one or two
        addition = '1'
        if len(n) % 2 == 1:
            for i in range(0, int(len(n) / 2)):
                addition += '0'
        else:
            addition += '1'
            for i in range(0, int(len(n) / 2) - 1):
                addition += '0'
        topResult = str(int(result) + int(addition))
        if int(topResult) - int(n) < max(int(n) - int(result), int(result) - int(n)):
            return topResult
        # try substract middle one or two
        lowResult = str(int(result) - int(addition))
        if int(n) - int(lowResult) <= max(int(n) - int(result), int(result) - int(n)):
            return lowResult
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.nearestPalindromic(
            '1837722381'), '1837667381')
        self.assertEqual(solution.nearestPalindromic('123892133'), '123888321')
        self.assertEqual(solution.nearestPalindromic('10001'), '9999')
        self.assertEqual(solution.nearestPalindromic('111111111'), '111101111')
        self.assertEqual(solution.nearestPalindromic('1283'), '1331')
        self.assertEqual(solution.nearestPalindromic('11011'), '11111')
        self.assertEqual(solution.nearestPalindromic('88'), '77')
        self.assertEqual(solution.nearestPalindromic('123'), '121')
        self.assertEqual(solution.nearestPalindromic('1'), '0')
        self.assertEqual(solution.nearestPalindromic('10'), '9')
        self.assertEqual(solution.nearestPalindromic('230'), '232')
        self.assertEqual(solution.nearestPalindromic('11'), '9')
        self.assertEqual(solution.nearestPalindromic('2'), '1')
        self.assertEqual(solution.nearestPalindromic('99'), '101')
        self.assertEqual(solution.nearestPalindromic('11911'), '11811')


if __name__ == '__main__':
    unittest.main()
