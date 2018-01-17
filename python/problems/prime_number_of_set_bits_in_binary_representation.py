"""
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

https://leetcode.com/submissions/detail/136523875/
"""


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        result = 0
        for i in range(L, R + 1):
            if isPrime(bin(i).count('1')):
                result += 1
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.countPrimeSetBits(6, 10), 4)
        self.assertEqual(solution.countPrimeSetBits(10, 15), 5)
        self.assertEqual(solution.countPrimeSetBits(567, 607), 21)
        self.assertEqual(solution.countPrimeSetBits(842, 888), 23)


if __name__ == '__main__':
    unittest.main()
