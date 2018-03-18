"""
From 0 to n, count how many factors in those numbers.


"""


class Solution:
    def countFactors(self, n, factor):
        """
        :type n: int
        :type factor: int
        :rtype: int
        """
        count = 0
        while n >= factor:
            n //= factor
            count += n
        return count


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.countFactors(2, 3), 0)
        self.assertEqual(solution.countFactors(4, 3), 1)
        self.assertEqual(solution.countFactors(6, 3), 2)
        self.assertEqual(solution.countFactors(4, 5), 0)
        self.assertEqual(solution.countFactors(5, 5), 1)
        self.assertEqual(solution.countFactors(25, 5), 6)
        self.assertEqual(solution.countFactors(26, 5), 6)


if __name__ == '__main__':
    unittest.main()
